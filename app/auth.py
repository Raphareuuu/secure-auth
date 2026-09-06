from argon2 import PasswordHasher

password_hasher = PasswordHasher()

#recebe a senha original e retorna o hash
def hash_password(password: str) -> str:
    return password_hasher.hash(password)

#recebe a senha que o usuário digitou e o hash que está armazenado no banco
def verify_password(password: str, password_hash: str) -> bool:
    try:
        password_hasher.verify(password_hash, password)
        return True
    except Exception:
        return False