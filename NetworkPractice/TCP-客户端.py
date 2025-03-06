from socket import *

client_socket = socket(AF_INET,SOCK_STREAM)
host_port = ("127.0.0.1",8081)

client_socket.connect(host_port)

send_data = input("请输入:")
client_socket.send(send_data.encode("utf-8"))

recv_data = client_socket.recv(1024)

print("服务端接收的数据：",recv_data.decode("utf-8"))
client_socket.close()

