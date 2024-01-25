import socket

HOST = '127.0.0.1'  # 服务器IP地址  
PORT = 5000  # 服务器端口号  

# 创建一个TCP套接字  
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器  
client_socket.connect((HOST, PORT))

print(f'已连接到服务器 {HOST}:{PORT}')

# 当连接处于打开状态  
while True:
    # 发送消息给服务器  
    message = input('请输入要发送的消息: ')
    client_socket.sendall(message.encode())

    # 接收服务器的回复  
    data = client_socket.recv(1024)
    print(f'收到服务器的回复: {data.decode()}')