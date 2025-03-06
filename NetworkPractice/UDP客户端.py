from socket import *


# socket.AF_INET：指定地址族（address family）。AF_INET 表示使用 IPv4 地址。
# socket.SOCK_STREAM：指定套接字类型。SOCK_STREAM 表示使用 TCP 协议，提供可靠的、面向连接的服务。
# 创建一个tcp协议的socket
# s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 创建一个udp协议的socket
# s2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#
# print(s2)

#创建一个udp的套接字 然后发送一条数据到网络上的另外一个进程

client_socket = socket(AF_INET,SOCK_DGRAM)

server_host_port = ('127.0.0.1',8081)

datas = input("请输入： xxxx").encode("utf8")

client_socket.sendto(datas,server_host_port)

print("send success")

client_socket.close()
