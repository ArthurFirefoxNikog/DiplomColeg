import pickle
import hashlib

class LAPE:
    def __init__(self, user_data_r: dict):
        self.__user_data_r = user_data_r

    @property
    def user_data_r(self):
        return self.__user_data_r
    
    def __hashing(self):

        hashed_data = {}

        for key, value in self.user_data_r.items():
            hashed_value = hashlib.sha256(value.encode()).hexdigest()
            hashed_data.setdefault(key, hashed_value)

        return hashed_data
    
    def __call__(self, *args, **kwds):
        return