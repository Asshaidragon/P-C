import socket
import datetime


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 5000))
server_socket.listen(5)
print('Server ready')


def logging(result):
    now = datetime.datetime.now()
    with open(f"{now.strftime('%d.%m.%y.log')}", "a") as f:
        f.write(result.decode('utf-8'))
        f.write('\n')


while True:
    try:
        client_socket, addr = server_socket.accept()
        logging(str(addr).encode())
    except KeyboardInterrupt:
        server_socket.close()
        break
    else:
        while True:
            result = client_socket.recv(4096)
            if result.decode('utf-8').lower() == 'end':
                client_socket.close()
                logging(('-' * 90).encode())
                break
            elif result.decode('utf-8')[0:5].lower() == 'error':
                print("CRITICAL ERROR:")
                print(result.decode('utf-8'))
                logging(result)
            else:
                logging(result)
                # print(result.decode('utf-8'))


