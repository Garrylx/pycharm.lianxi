"""author = "GARRY GY"
Date:2020-12-03

"""
#原字符 转义字符
print("sssss\tddddd")
print("ssss\tdddd")#空位输出
print("ssss\rdddd")#覆盖输出
print("ssss\bdsa")#覆盖上一位输出
print(r"sssss\ndsd")#r为原字符，取消转义字符的功能
print("sssss\ndddddd")#转义字符

print(chr(0b1000111011000001))#unicode转为中文字符   必须加0b  八进制加0o 十六进制加0x 默认为十进制
print(ord("高"))#ord（）转为十进制字符编码

