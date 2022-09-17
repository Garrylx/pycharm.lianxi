"""author = "GARRY GY"
Date:2021-02-01

"""
import urllib.request
import urllib.parse
import string
def get_params():
    url = "https://www.baidu.com/s?wd="

    params = {
        "wd":"zhongwen",
        "key":"zhang",
        "value":"san"

    }
    str_params = urllib.parse.urlencode(params)
    print(str_params)
    final_url = url + str_params
    #将带有中文的url转移成计算机可识别的url
    end_url = urllib.parse.quote(final_url,safe=string.printable)

    response = urllib.request.urlopen(end_url)

    data = response.read().decode("utf-8")

    print(data)

get_params()
