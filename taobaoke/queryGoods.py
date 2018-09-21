import top.api
import requests
import json

productionUrl = "https://eco.taobao.com/router/rest"
appkey = "25083490"
secret = "77068d785fb6dc77d1865dc0737e1684"
port = 80
pid = "28940900149"

# url		原始网址
# url1    干净的商品链接，去除pid
# native_url	移动端调起地址
def taoKouLingChangeHTTP(tkl):
    params = {"tkl":tkl,"user_key":"1gQODe4MGwToFY0j"}
    resp = requests.get("http://api.kfsoft.net/api/tb/tklQuery/v1.php",params)
    dict = resp.json()
    print(dict)

def httpChangeTuiguangWeb(goodsUrl):



#taoKouLingChangeHTTP("【程序员的数学1-2-3 线性代数+概率统计全套3本书 算法基础入门教程 计算机软件开发编程教程 机器学习数学算法程序设计教材书】，復·制这段描述￥Y8L4bV3nX6i￥后到👉淘♂寳♀👈[来自超级会员的分享]")
