import socket


def connect():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('127.0.0.1', 5000))

    hostname = socket.gethostname()
    server_socket.send(hostname.encode('utf-8'))
    while True:
        log_text = input().encode('utf-8')
        if log_text.decode('utf-8') == 'end':
            log = socket.gethostname() + log_text
            server_socket.send(log)
            server_socket.close()
            break
        else:
            # log_text = log_text.encode('utf-8')
            server_socket.send(log_text)



    # x = input().encode('utf-8')
# .decode('utf-8')

connect()