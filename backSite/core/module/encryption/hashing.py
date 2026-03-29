import hashlib

class Hashing:

    def __call__(self, meaning: str = None):
        
        if isinstance(meaning, str) and meaning:
            return hashlib.sha256(meaning.encode("utf-8")).hexdigest()

        return None
    
