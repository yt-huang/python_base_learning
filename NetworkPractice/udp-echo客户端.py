from socket import *




#客户端可以发送多条数据，2客户端如果发送了exit 则客户端退出3服务器收到什么就返回什么

client_socket = socket(AF_INET,SOCK_DGRAM)

server_host_port = ('127.0.0.1',8081)

while True:
    datas = input("请输入： xxxx，如果输入exit表示客户端退出").encode("utf8")
    if datas.decode("utf8") == "exit":
        break
    client_socket.sendto(datas,server_host_port)
    print("send success")
    datas,server_host_port = client_socket.recvfrom(1024)
    print("服务器返回这信息：",datas.decode('utf8'))
client_socket.close()
