import re

class IsPasswordVerification:

    """
    Eng:
        Class for password verification.
        Checks if the password meets the following criteria:
            1. At least 8 characters long.
            2. Contains at least one uppercase letter.
            3. Contains at least one lowercase letter.
            4. Contains at least one digit.
            5. Contains at least one special character.
            6. If confirmation is provided, it must match the password.
            7. Password cannot be only whitespace.
            8. Returns True if all criteria are met, otherwise False.
            9. If confirmation is None, it is not checked.

    Ru:
        Класс для проверки пароля.
        Проверяет, соответствует ли пароль следующим критериям:
            1. Его длина не менее 8 символов.
            2. Содержит как минимум одну заглавную букву.
            3. Содержит как минимум одну строчную букву.
            4. Содержит как минимум одну цифру.
            5. Содержит как минимум один специальный символ.
            6. Если подтверждение получено, оно должно совпадать с паролем.
            7. Пароль не может состоять только из пробелов.
            8. Возвращает значение True, если соблюдены все критерии, в противном случае значение False.
            9. Если подтверждения нет, оно не проверяется.
    """

    def __init__(self):
        self.pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^\w\s]).{8,}$"

    def validate_password(
                          self,
                          password: str=None, 
                          confirm: str=None
                          ):
        if not isinstance(password, str) or password.strip() == "":
            return False

        if not re.match(self.pattern, password):
            return False

        if confirm is not None and password != confirm:
            return False

        return True