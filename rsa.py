import random


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime_number(length):
    while True:
        # Генерируем случайное число с нужной длиной
        num = random.randint(10 ** (length - 1), 10 ** length - 1)

        # Проверяем, является ли число простым
        if is_prime(num):
            return num


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def generate_keypair(bits):
    # Генерируем два простых числа
    p = generate_prime_number(bits)
    print(f'p = {p}')
    q = generate_prime_number(bits)
    print(f'q = {q}')

    # Вычисляем модуль n и функцию Эйлера
    n = p * q
    print(f'n = {n}')
    phi = (p - 1) * (q - 1)
    print(f'phi = {phi}')

    # Выбираем открытый ключ e (1 < e < phi) и вычисляем закрытый ключ d
    e = random.randint(1, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi - 1)

    print(f'e = {e}')

    d = mod_inverse(e, phi)
    print(f'd = {d}')

    return ((n, e), (n, d))


def encrypt(message, public_key):
    n, e = public_key
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text


def decrypt(cipher_text, private_key):
    n, d = private_key
    decrypted_text = [chr(pow(char, d, n)) for char in cipher_text]
    return ''.join(decrypted_text)


# Пример использования
# message = input("Your msg: ")
# prime_len = int(input("Prime number len: "))
# public_key, private_key = generate_keypair(prime_len)
# print(f'Public key: {public_key}\nPrivate key: {private_key}')
#
# # Шифрование
# encrypted_message = encrypt(message, public_key)
# print("Зашифрованное сообщение:", encrypted_message)
#
# # Дешифрование
# decrypted_message = decrypt(encrypted_message, private_key)
# print("Расшифрованное сообщение:", decrypted_message)
