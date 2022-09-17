"""author = "GARRY GY"
Date:2021-03-23

"""
import socket
import threading #多线程

server = socket.socket()
#绑定到0.0.0.0 8000端口上
server.bind(("0.0.0.0",16))
server.listen()

def handle_sock(sock,addr):
    sock.send("welcome to server".encode("utf8"))
    tmp_data = sock.recv(1024)
    print(tmp_data.decode("utf8"))
    input_data = input()
    sock.send(input_data.encode("utf8"))


#获取客户端进行多线程处理
while True:
    sock, addr = server.accept()

    #启动一个线程去连接
    client_thread = threading.Thread(target=handle_sock,args=(sock,addr))
    client_thread.start()

#阻塞等待连接
sock,addr = server.accept()
data = ""
while True:
    sock.send("welcome to server".encode("utf8"))
    tmp_data = sock.recv(1024)
    print(tmp_data.decode("utf8"))
    input_data = input()
    sock.send(input_data.encode("utf8"))
    if tmp_data:
        data += tmp_data.decode("utf-8")
        if tmp_data.decode("utf8").endswith("#"):
            break
    else:
        break

print(data)
sock.close()
