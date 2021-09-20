#串接、擷取公開資料
import urllib.request as request
import json
src="https://data.taipei/api/v1/dataset/5738e1ed-41f0-4205-adfe-7377be708193?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response)
#將市場名稱列出來
clist=data["result"]["results"]
with open("market.txt","w",encoding="utf-8") as file:
    for market in clist:
        file.write(market["stitle"]+"\n")