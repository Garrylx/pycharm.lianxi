"""author = "GARRY GY"
Date:2021-03-23

"""
#client(客户)
import socket
client = socket.socket()
client.connect(("10.191.188.33",16))#本地IP，端口
server_data = client.recv(1024)
print("server response:{}".format(server_data.decode("utf-8")))
while True:

    while True:
        input_data = input("please input")

        client.send(input_data.encode("utf-8"))
        server_data = client.recv(1024)
        print("server response:{}".format(server_data.decode("utf-8")))
#client.close()