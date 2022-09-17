"""author = "GARRY GY"
Date:2021-02-02

"""
import urllib.request

def proxy_user():

    proxy = [
        {"http":"223.242.225.91"},
        {"http":"27.43.190.196"},
        {"http":"42.7.31.198"},
        {"http":"27.43.191.231"}
    ]

    for i in proxy:
        print(i)
        #利用遍历出来的IP创建处理器
        proxy_handler = urllib.request.ProxyHandler(i)
        #创建opener
        opener = urllib.request.build_opener(proxy_handler)

        try:
            opener.open("https://www.baidu.com",timeout = 1)
            print("hh")

        except Exception as e:
            print(e)

proxy_user()