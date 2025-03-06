import socket
from socket import *




#客户端可以发送多条数据，2客户端如果发送了exit 则客户端退出3服务器收到什么就返回什么



socketserver = socket(AF_INET,SOCK_DGRAM)

host_port = ('127.0.0.1',8081)

socketserver.bind(host_port)

while True:
    datas = socketserver.recvfrom(1024)
    print(datas[0].decode('utf8'))
    print(datas[1])
    socketserver.sendto(datas[0],datas[1])
    if datas[0].decode('utf8') == "exit":
        break

socketserver.close()