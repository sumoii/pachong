#!/user/bin/python3
# -*- codeing = utf-8 -*-
import requests
import parsel
url='https://www.ximalaya.com/xiangsheng/35105051/'
headers= {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}
req = requests.get(url=url,headers=headers)
html_data = req.text

selector = parsel.Selector(html_data)
lis = selector.xpath('//div[@class="sound-list _is"]/ul/li')

for li  in lis :
    title = li.xpath('.//a/@title').get()
    href =li.xpath('.//a/@href').get()
    print(title,href)