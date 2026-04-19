from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('form_login/', views.form_login, name='login'),
    path('form_register/', views.form_register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout_view, name='logout')
]