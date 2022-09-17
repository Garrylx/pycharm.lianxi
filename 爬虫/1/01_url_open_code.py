"""author = "GARRY GY"
Date:2021-01-27

"""
import urllib.request

def load_date():
    url = "http://www.baidu.com/"#get请求 http请求
    response = urllib.request.urlopen(url)#response是http相应的访问对象
    print(response)
    #读取内容  bytes类型（二进制）
    date = response.read()
    print(date)
    #将文件获取的内容转换为字符串
    str_date = date.decode("utf-8")
    print(str_date)
    #将数据写入文件
    with open("baidu.html", "w", encoding="utf-8") as f:
        f.write(str_date)
    #将字符串类型转化为bytes
    #python 爬取的类型：str bytes
    #如果爬取的为bytes类型：但需要字符串，用decode（“utf-8”）
    #相反则用encode（“utf-8”）



load_date()