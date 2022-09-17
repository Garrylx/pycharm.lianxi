"""author = "GARRY GY"
Date:2021-02-02

"""
import urllib.request

def create_proxy_hander():
    url = "https://www.csdn.net/"

    #添加代理
    proxy = {
        #免费的写法
        "http":"223.242.225.91:9999"
    }
    #代理的处理器
    proxy_hander = urllib.request.ProxyHandler(proxy)

    #穿件自己的opener
    opener = urllib.request.build_opener(proxy_hander)

    #用代理IP发送请求
    data = opener.open(url).read()
    print(data)

create_proxy_hander()