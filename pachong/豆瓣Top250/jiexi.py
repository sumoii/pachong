# from bs4 import BeautifulSoup
# import re
# file = open ("./baidu.html","rb")
# html = file.read()
# bs = BeautifulSoup(html,"html.parser")

# print(bs.prettify())
# print(bs.title)
# print(bs.title.name) # 获取title标签的文本内容
# print(bs.title.string) # 获取title标签的所有内容
# print(bs.find(id="u1"))
# for item in bs.find_all("a"):
#     print(item.get("href"))
# for item in bs.find_all("a"):
#     print(item.get_text())
# 在这里，我们把 a 标签的所有属性打印输出了出来，得到的类型是一个字典。
# print(bs.a.attrs)
# bs.a['class'] = "newClass"
# print(bs.a)
# del bs.a['class']
# print(bs.a)
# print(bs.a.attrs)
# print(bs.head.contents)
# for child in bs.body.children:
#     print(child)
# t_list = bs.find_all(["meta","link"])
# for item in t_list:
#     print(item)
# t_list = bs.find_all(re.compile("nk"))
# for item in t_list:
#     print(item)
# def name_is_exists(tag):
#     return tag.has_attr("link")
# t_list = bs.find_all(name_is_exists)
# for item in t_list:
#     print(item)
# t_list = bs.find_all(id="head")
# print(t_list)
# t_list = bs.find_all(href=re.compile("http://news.baidu.com"))
# print(t_list)
# t_list = bs.find_all(class_=True)
# for item in t_list:
#     print(item)
# t_list = bs.find_all(text="hao123")
# for item in t_list:
#     print(item)
# t_list = bs.find_all(text=["hao123", "地图", "贴吧"])
# for item in t_list:
#     print(item)
# t_list = bs.find_all(text=re.compile("\d"))
# for item in t_list:
#     print(item)
# def length_is_two(text):
#     return text and len(text) == 2
# t_list = bs.find_all(text=length_is_two)
# for item in t_list:
#     print(item)
# t_list = bs.select("head > title")
# print(t_list)
# t_list = bs.select(".mnav ~ .bri")
# print(t_list)
baseurl = 'https://www.ximalaya.com/xiangsheng/35105051/'
for i in range(1,13):
    url = baseurl +f"p{i}"
    print (url)
