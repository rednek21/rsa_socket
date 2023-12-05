import socket
import pickle

from rsa import encrypt


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Получение открытого ключа от сервера
    server_public_key = pickle.loads(client_socket.recv(1024))

    while True:
        message = input("Введите сообщение для отправки (введите 'exit' для выхода): ")

        if message.lower() == 'exit':
            break

        # Шифрование сообщения перед отправкой
        encrypted_message = pickle.dumps(encrypt(message, server_public_key))
        client_socket.send(encrypted_message)

    client_socket.close()


start_client()
