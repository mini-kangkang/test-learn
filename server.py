import socket

HOST = '127.0.0.1'  # 服务器IP地址
PORT = 5000  # 服务器端口号

# 创建一个TCP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址和端口号
server_socket.bind((HOST, PORT))

# 开始监听客户端连接
server_socket.listen()

print(f'服务器已启动，等待客户端连接...')

# 当有客户端连接时
while True:
    # 接受客户端连接
    client_socket, address = server_socket.accept()
    print(f'客户端 {address} 已连接.')

    # 当连接处于打开状态
    while True:
        # 接收客户端发送的消息
        data = client_socket.recv(1024)
        if not data:
            break

            # 打印接收到的消息
        print(f'收到客户端 {address} 的消息: {data.decode()}')

        # 发送消息给客户端
        message = input('请输入回复消息: ')
        client_socket.sendall(message.encode())

        # 关闭连接
    client_socket.close()