from datetime import datetime, timedelta, timezone
from jose import jwt
from core.settings import config
from passlib.context import CryptContext
import bcrypt 

# pwd_context = CryptContext(schemes=["argon2"])


class PassHash:
    def __init__(self) -> None:
        self.pwd_context = CryptContext(schemes=["bcrypt"])
        
    
    def get_hash_password(self, plain_password: str) -> str:
        byte_string = bcrypt.hashpw(password=plain_password.encode("utf-8"), salt=bcrypt.gensalt(12))
        print("BYTE : ", byte_string)
        return byte_string.decode('utf-8')
        return self.pwd_context.hash(plain_password)
    
    def verify_password(self, plain_password: str, hash_password: str) -> bool:
        return bcrypt.checkpw(password=plain_password.encode("utf-8"), hashed_password= hash_password.encode("utf-8"))
        # return bcrypt.verify(plain_password, hash_password)
        # return plain_password == hash_password
        return self.pwd_context.verify(plain_password, hash_password)
        # return bcrypt.checkpw(plain_password.encode('utf-8'), hash_password.encode('utf-8'))

    def create_access_token(self, data_to_encode: dict, expires_delta: timedelta | None = None) -> str:
        to_encode = data_to_encode.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else :
            expire = datetime.now(timezone.utc) + timedelta(days=2) 
        to_encode.update({ 'exp': expire })
        encoded_jwt = jwt.encode(claims=to_encode,key= config.JWT_SECRET_KEY, algorithm= config.JWT_ALGORITHM)
        return encoded_jwt
    
    def check_acces_token(self, access_token: str) -> bool:
        try :
            payload = jwt.decode(access_token,config.JWT_SECRET_KEY,algorithms=[config.JWT_ALGORITHM])
            return True
        except Exception as e:
            print("error: ", e)
            return False
