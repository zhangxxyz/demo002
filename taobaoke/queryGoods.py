import top.api

productionUrl = "https://eco.taobao.com/router/rest"
appkey = "25083490"
secret = "77068d785fb6dc77d1865dc0737e1684"
port = 80

req=top.api.TbkItemGetRequest(productionUrl,port)
req.set_app_info(top.appinfo(appkey,secret))
req.fields="num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick"
req.q="女装"
req.cat="16,18"
req.itemloc="杭州"
req.sort="tk_rate_des"
req.is_tmall= "0"
req.is_overseas="0"
req.start_price=10
req.end_price=10
req.start_tk_rate=123
req.end_tk_rate=123
req.platform=1
req.page_no=123
req.page_size=20
try:
	resp= req.getResponse()
	print(resp)
except Exception as result:
	print(result)