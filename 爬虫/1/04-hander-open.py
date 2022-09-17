"""author = "GARRY GY"
Date:2021-02-02

"""
import urllib.request

def hander_openner():
    #系统的urlopen并没有添加代理的功能所以我们要自定义这个功能
    #安全 套接层 ssl第三方的CA数字证书
    #url为什么可以请求数据--handler处理器
    #自己的openner请求数据
    #urllib.request.urlopen()

    url = "https://www.csdn.net/"

    #创建自己的处理器
    hander = urllib.request.HTTPHandler()

    #创建自己的opener
    opener = urllib.request.build_opener(hander)

    #用自己创建的方法调用open请求数据
    response = opener.open(url)
    data = response.read()
    print(response)
    print(data)

hander_openner()
