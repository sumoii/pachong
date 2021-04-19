#!/user/bin/python3
# -*- codeing = utf-8 -*-
import requests
import jsonpath
url='https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=1&tagAll=0&page=1'

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"
}
response = requests.get(url=url,headers=headers).json()
img_list = jsonpath.jsonpath(response,'$..screenshot')
for index,img_url in enumerate(img_list):
    img_data = requests.get(img_url).content
    file_name = 'lol/' +  str(index+1) + '.jpg'
    with open(file_name,'wb') as f:
        f.write(img_data)
        f.close()




