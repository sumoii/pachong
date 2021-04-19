#!/user/bin/python3
# -*- codeing = utf-8 -*-
import re
findimg =re.compile(r'<img.*src="(.*?)"',re.S)
findtitle =re.compile(r'<span class="title">(.*)</span>')
f1 =open("miove.html", 'rb')
item = f1.read()
item = str (item)
print(item)
img = re.findall(findimg,item)[0]
print (img)
print(re.findall(findtitle,item))


# if (len(titles) == 2):
#     ctitle = titles[0]
#     data.append(ctitle)
#     otitle = titles[1].replace("/"," ")
#     data.append(otitle)
# else:
#     data.append(titles)
#     data.append('')
