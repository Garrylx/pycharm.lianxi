"""author = "GARRY GY"
Date:2021-02-01

"""
import urllib.request

def load_baidu():
     url = "http://www.baidu.com"
     header = {
          #浏览器的版本
          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
     }

     #创建请求对象
     request = urllib.request.Request(url,headers=header)
     #可用方法动态添加head信息（把前面的headers=header去掉）
     request.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
     )
     #请求网络数据(不在此处增加请求头信息，应为没有提供参数)
     response = urllib.request.urlopen(request)
     print(response)
     data = response.read().decode("utf-8")

     #获取完整的url
     a_url = request.get_full_url()
     print(a_url)

     #响应头
     #print(response.headers)
     #获取请求头信息
     request_headers = request.headers
     print(request_headers)

     #第二种方法打印请求头信息get_header方法(注意除了首字母需要大写其他的都小写)
     request_headers = request.get_header("User-agent")

     with open("02header.html", "w") as f:
         f.write(data)

load_baidu()
