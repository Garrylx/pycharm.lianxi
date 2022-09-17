"""author = "GARRY GY"
Date:2021-01-27

"""
#url  是因特网的万维网服务程序上用于指定信息位置的表示方法  uniform resource locator;URL

import urllib.request,urllib.parse,string


def get_method_params():

    url = "http://www.baidu.com/s?wd="
    #拼接字符串
    name = "美女"
    final_url = url + name
    #使用代码发送网络请求，但是代码有汉字ascii没有汉字；url转义
    #将包含汉字的网址进行转义
    new_code_url = urllib.parse.quote(final_url,safe=string.printable)
    print(new_code_url)

    response = urllib.request.urlopen(new_code_url)
    print(response)
    #读取内容
    data = response.read().decode()
    print(data)
    #保存到本地
    with open("02_encode.html", "w", encoding="utf-8") as f:
        f.write(data)
    #UnicodeEncodeError: 'ascii' codec can't encode characters in
    # position 10-11: ordinal not in range(128)
    #python是解释型语言；解析器只支持ascii 0 -127  ------不支持中文
get_method_params()