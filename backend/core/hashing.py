from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hasher:
    @staticmethod
    def verify_password(plain_password:str, hashed_password:str) -> bool:
        """ Is the password valid? """
        return pwd_context.verify(plain_password, hashed_password)
    
    @staticmethod
    def get_password_hash(password:str) -> str:
        """ Generate a password hash. """
        return pwd_context.hash(password)
