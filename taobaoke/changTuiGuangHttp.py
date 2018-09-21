#没有api权限 自主用爬虫获取推广链接
import requests
import json
UA = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
proxies = {"http":"110.73.11.207:8123"}
cook ="t=41255459c909c67fe58e0a133ad6e57b; cookie2=1528a1d73a19cfe5b27c1b4947fe9edd; _tb_token_=5e756743137a9; cna=nmErFB+TcwcCAW/GGPaoOXy+; isg=BFNTlZhWDN4brcAKhj-5cbbF4dG9oOei3AnFJAVxynKkhHQmi9qNG6CWujxPPz_C; JSESSIONID=765BDFC235F832B878FF096B98ED039B; account-path-guide-s1=true; v=0; alimamapwag=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTAuMTM7IHJ2OjYzLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvNjMuMA%3D%3D; cookie32=6e353e44dcb2ada023d98f7c1d920912; alimamapw=GwkHX1YIAgEEBFsEAgE5VgVWVVcHBgYAVwcGDlBXUwhTVQcBUgNXBgBWAQNVUgA%3D; cookie31=MzI5MDAxNDUsemhhbmc4NzM1MzkwNzksODk2OTk4MDFAcXEuY29tLFRC; login=VT5L2FSpMGV7TQ%3D%3D; apush33cf35cc5200d8c89f65e8649c606a77=%7B%22ts%22%3A1537509985282%2C%22parentId%22%3A1537509952169%7D"
# http://item.taobao.com/item.htm?id=557635861446
requestUrl = "https://pub.alimama.com/urltrans/urltrans.json?siteid=122500185&adzoneid=28940900149&promotionURL=http://item.taobao.com/item.htm?id=557635861446&t=1537510754204&pvid=52_111.198.24.246_346_1537510741562&_tb_token_=5e756743137a9&_input_charset=utf-8"

Cookies ={}

def getCookiesDict():
    if len(Cookies)>0:
        return Cookies
    for dict in cook.split(";"):
        key,value = dict.split('=',1)
        Cookies[key] = value
    return Cookies

def getHttp():
    res = requests.get(requestUrl,proxies=proxies,cookies=getCookiesDict(),headers=UA)
    dict=res.json()
    print(dict)
getHttp()


