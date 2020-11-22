import socket
import os
import time

def start_script(path_to_folder='C:\\1'):
    while True:
        if len(os.listdir(path_to_folder)) != 0:
            time.sleep(2)
            cnt_of_files = len(os.listdir(path_to_folder))
            client_message = 'Error! ' + 'найдено файлов: ' + str(cnt_of_files)
            break
    return client_message

def connect():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_socket.connect(('DESKTOP-24EDK13', 5002))
    server_socket.connect(('127.0.0.1', 5000))
    hostname = socket.gethostname()
    server_socket.send(hostname.encode('utf-8'))
    while True:
        message = server_socket.recv(4000)
        print(message.decode())
        if message == b'start_scan':
            result = start_script()
            print(result)
        else:
            result = 'unknown command'
            print('unknown command')
            #server_socket.send(b'unknown command')

        server_socket.send(result.encode())
        log_text = input().encode('utf-8')
        if log_text.decode('utf-8').lower() == 'end':
            server_socket.send(log_text)
            server_socket.close()
            break
        else:
            # log_text = log_text.encode('utf-8')
            server_socket.send(log_text)





connect()