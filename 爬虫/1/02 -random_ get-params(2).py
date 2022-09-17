"""author = "GARRY GY"
Date:2021-02-01

"""
import urllib.request
import random

def load_browsers():
    url = "http://www.baidu.com"

    user_agent = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
                  "Mozilla / 5.0(Windows NT 6.1;WOW64;rv: 6.0) Gecko / 20100101Firefox / 6.0",
                  "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)",

    ]
    #每次请求都是不一样的浏览器
    random_user_agent = random.choice(user_agent)
    #创建请求对象
    request = urllib.request.Request(url)

    #增加对应的请求头信息
    request.add_header("User-agent",random_user_agent)

    #请求数据
    response = urllib.request.urlopen(request)
    #请求头信息
    print(request.get_header("User-agent"))

load_browsers()