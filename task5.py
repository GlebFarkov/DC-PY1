import random

def get_random_password(length: int) -> str:
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

print(get_random_password(int(input('Введите длину пароля: '))))
