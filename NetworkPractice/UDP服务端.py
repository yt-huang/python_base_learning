from socket import *

# 创建一个服务端的socket 接受udp的客户端的信息
socket_server = socket(AF_INET,SOCK_DGRAM)
# 绑定ip和端口
host_port = ('127.0.0.1',8081)

# 服务器端的socket绑定ip和端口

socket_server.bind(host_port)

# 接受客户端发送过来的数据 每次接收1kb的数据，返回得到数据data
datas = socket_server.recvfrom(1024)

print(datas[0].decode("utf-8"))


# 关闭套接字释放资源

socket_server.close()