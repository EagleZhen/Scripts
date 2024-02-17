import requests
from lxml import etree
from urllib.parse import urlencode
from request_html import HTML

song_id="536624791"
# url = "https://music.163.com/#/song?id="+song_id+"&userid=417214757"
url="https://movie.douban.com/"

f1=open("D:/Github/Scripts/fill in mp3 info from ncm/test.html",'w')
f2=open("D:/Github/Scripts/fill in mp3 info from ncm/test1.html",'w')

# ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"

# with requests.request('GET',url,headers = {'User-agent':ua}) as res:
#     content = res.text          #获取HTML的内容
#     html = etree.HTML(content)  #分析HTML，返回DOM根节点

#     # orders = html.xpath("//div[@class='billboard-bd']//tr/td[@class='order']/text()")
#     # titles = html.xpath( "//div[@class='billboard-bd']//td//a/text()")  #使用xpath函数，返回文本列表
#     # print(orders,file=f1)
#     # print(titles,file=f1)

#     # title = html.xpath("/html/body/div[4]/div[1]/div/div[3]/div[5]/div[2]/table/tbody/tr[1]/td[1]/text()")
#     title = html.xpath("//div[@class='aside']//div[@id='doulist']//a/text()")
#     print (title)

#     # ans = dict(zip(orders,titles)) #豆瓣电影之本周排行榜
#     # for k,v in ans.items():
#     #     print(k,v,file=f1)
 
with open()