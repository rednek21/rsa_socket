import pickle
import socket

from rsa import decrypt, generate_keypair


def start_server(prime_len):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print("Сервер слушает на порту 12345...")

    connection, client_address = server_socket.accept()
    print("Подключено к клиенту:", client_address)

    # Генерация ключей RSA
    server_public_key, server_private_key = generate_keypair(prime_len)
    print(f'Public key: {server_public_key}\nPrivate key: {server_private_key}')

    # Отправка открытого ключа клиенту
    connection.send(pickle.dumps(server_public_key))

    try:
        while True:
            data = connection.recv(1024)
            if not data:
                break

            # Дешифрование полученных данных
            encrypted_message = pickle.loads(data)
            print(f'Полученное сообщение: {encrypted_message}')
            decrypted_message = decrypt(encrypted_message, server_private_key)

            print("Дешифрованное сообщение:", decrypted_message)

    finally:
        connection.close()


prime_len = int(input("Input len for prime generator: "))
start_server(prime_len)

