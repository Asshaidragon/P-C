import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_socket.bind(('MASTER-PC01', 5000))
server_socket.bind(('127.0.0.1', 5000))
server_socket.listen(5)

while True:
    try:
        print('Server ready')
        client_socket, addr = server_socket.accept()
        print('connection from', addr)
    except KeyboardInterrupt:
        server_socket.close()
        break
    else:
        while True:
            result = client_socket.recv(4096)
            if result.decode('utf-8') == 'end':
                client_socket.close()
                break
            elif result.decode('utf-8')[0:5] == 'ERROR':
                print("Critical pizdec")
            else:
                with open("file.txt", "a") as f:
                    f.write(result.decode('utf-8'))
                    f.write('\n')




