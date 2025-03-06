from socket import *
# tcp协议
server_socket = socket(AF_INET,SOCK_STREAM)
host_port = ("",8081)
server_socket.bind(host_port)
server_socket.listen(10)
# 线程客户端的链接请求，当前函数是线程阻塞的函数
new_socket,client_addr = server_socket.accept()

data = new_socket.recvfrom(1024)

print(data[0].decode("utf-8"))

new_socket.send("hello".encode("utf-8"))

new_socket.close()
server_socket.close()