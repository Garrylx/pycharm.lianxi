"""author = "GARRY GY"
Date:2021-03-27

"""
# server
#1.处理转发消息
#2. 处理登录
#3，处理退出
#4. 维护历史消息，维护在线用户和维护用户的连接
import threading
import socket
from collections import defaultdict
import json


#client connect
online_user = defaultdict(dict)

#历史消息
user_message = defaultdict(list)

server = socket.socket()



#绑定IP
server.bind("10.172.24.110",16)
server.listen()

def s_hander(sock,addr):
    data = sock.recv(1024)
    json_data = json.loads(data.decode("utf-8"))
    action = json_data.get("action","")

    if action == "login":
        online_user[json_data["user1"]] = sock
        sock.send("success login in".encode("utf8"))
    elif action ==  "history_msg":
        sock.send(json.dumps())







while True:#阻塞等待连接
    sock,addr = server.accept()
#创建线程等待连接
    client_thread = threading.Thread(target=s_hander,args= (sock,addr))