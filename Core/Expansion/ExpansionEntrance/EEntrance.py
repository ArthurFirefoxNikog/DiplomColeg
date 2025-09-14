import ctypes
import os

class ExpansionEntrance:

    @staticmethod
    def isCheckPasPunctuation(password: str) -> bool:

        """Проверяет, содержит ли пароль хотя бы один специальный символ."""

        dll_path = os.path.join(os.path.dirname(__file__), 'checkPasPunctuation.dll')
        lib = ctypes.CDLL(dll_path)  # Загрузка DLL по абсолютному пути

        lib.checkPasPunctuation.argtypes = [ctypes.c_char_p]  # Указание типов аргументов
        lib.checkPasPunctuation.restype = ctypes.c_bool  # Указание типа возвращаемого значения
        return lib.checkPasPunctuation(password.encode('utf-8'))  # Вызов функции из DLL