"""author = "GARRY GY"
Date:2021-08-08
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
import socket


if __name__ == "__main__":

    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # sock_stream表示tcp类型
    tcp_socket.connect(("223.89.109.98",8000))
    x = input("please connect with me")
    x.encode("utf-8")
    tcp_socket.send(x)
    tcp_socket.close()