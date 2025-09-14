from Core.Expansion.ExpansionEntrance import EEntrance

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

    def __init__(self,
                 password: str, 
                 confirmation: str = None):

        self.__password = password
        self.__confirmation = confirmation

    @property
    def password(self):
        return self.__password
    
    @property
    def confirmation(self):
        return self.__confirmation

    def __password_cheker(self):

        results = (
            [], [], []
        )

        for char in self.password:
            results[0].append(char.isdigit())
            results[1].append(char.isupper())
            results[2].append(char.islower())

        for result in results:
            yield any(result)

    def __call__(self):

        if self.password.isspace():
            return False

        ASO_checks = (
            self.password == self.confirmation if bool(self.confirmation) else True,
            len(self.password) >= 8,
            all(self.__password_cheker()),
            EEntrance.ExpansionEntrance.isCheckPasPunctuation(self.password)
        )

        return all(ASO_checks)





