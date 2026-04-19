from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.cache import cache
from core.models import LoginLog
from core.utils import is_rate_limited
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

def get_client_ip(request):
    xff = request.META.get('HTTP_X_FORWARDED_FOR')
    if xff:
        return xff.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')

def get_user_agent(request):
    return request.META.get('HTTP_USER_AGENT', 'Unknown')

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def form_login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        now = timezone.now()

        username = request.POST.get("username")
        password = request.POST.get("password")

        ip = get_client_ip(request)

        ip_key = f"rate_ip_{ip}"
        username_key = f"rate_username_{username}"

        if is_rate_limited(ip_key, 5, 60) or is_rate_limited(username_key, 5, 60):
            return render(request, "form/form_login.html", {
                "error": "Слишком много попыток. Подождите минуту."
            })

        user = User.objects.filter(username=username).first()

        if not user:
            return render(request, "form/form_login.html", {
                "error": "Пользователь не найден"
            })
        
        if user.locked_until and user.locked_until > now:
            return render(request, "form/form_login.html", {
                "error": "Аккаунт временно заблокирован. Попробуйте позже."
            })

        auth_user = authenticate(request, username=username, password=password)
        print("AUTH USER:", auth_user)

        if auth_user:
            cache.delete(ip_key)
            cache.delete(username_key)

            user.failed_login_attempts = 0
            user.locked_until = None
            user.save()

            login(request, auth_user)

            LoginLog.objects.create(
                user=auth_user,
                ip=ip,
                user_agent=get_user_agent(request)
            )

            return redirect('profile')
        else:
            user.failed_login_attempts += 1

            if user.failed_login_attempts >= 5:
                user.locked_until = now + timedelta(minutes=5)

            user.save()
            return render(request, "form/form_login.html", {
                "error": "Неверный пароль"
            })

    return render(request, "form/form_login.html")

def form_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        email = request.POST.get('email')

        if not email or not password or not username:
            return render(request, 'form/form_register.html', {
                "error": "Заполните все поля"
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'form/form_register.html', {
                "error": "Email уже используется"
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'form/form_register.html', {
                "error": "Username уже занят"
            })
        
        if not password_confirm:
            return render(request, 'form/form_register.html', {
                "error": "Нету пароля для потверждения"
            })
        
        if password != password_confirm:
            return render(request, 'form/form_register.html', {
                "error": "Пароли не совпадают"
            })

        user = User.objects.create_user(
            email=email,
            username=username,
            password=password
        )

        group, _ = Group.objects.get_or_create(name="User")
        user.groups.add(group)

        login(request, user)
        return redirect('profile')

    return render(request, 'form/form_register.html')


@login_required
def profile(request):
    print(LoginLog.objects.all())
    last_log = LoginLog.objects.filter(user=request.user).last()
    return render(request, "rest/profile.html", {
        "user": request.user,
        "last_user_agent": last_log.user_agent if last_log else "Unknown"
    })

@login_required
def index(request):

    if request.user.groups.filter(name="Admin").exists():
        return redirect('/admin-panel/')
    
    return render(request, 'index.html')