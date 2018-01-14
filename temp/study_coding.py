"""
    python 编码/解码
    https://www.cnblogs.com/evening/archive/2012/04/19/2457440.html
    在python中使用decode()和encode()来进行解码和编码，使用unicode类型作为编码的基础类型。
    即：decode --> encode  |  str --> unicode --> str
    在python3中，取消了unicode类型。
"""
import codecs

my_str = "你好"
encode_str = my_str.encode("gbk")
print(encode_str)
decode_str_1 = encode_str.decode("gbk")
print(decode_str_1)

decode_str_2 = encode_str.decode("gb2312")
print(decode_str_2)
try:
    decode_str_3 = encode_str.decode("utf-8")
    print(decode_str_3)
except UnicodeDecodeError as err:
    print(str(err))

with open("data/study_coding/test.txt", "r") as f:
    input_data = f.read()
    print(input_data)
    pass

with codecs.open("data/study_coding/test.txt", "r", encoding="gbk") as f:
    input_data = f.read()
    print(input_data)
