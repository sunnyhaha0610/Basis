#JSON格式
import  json
#讀取
with open("config.json",mode="r") as file:
    data=json.load(file)
print(data) #data是一個字典資料
print("name:",data["name"])
print("version:",data["version"])
#修改
data["name"]="New Name" 
#寫入
with open("config.json",mode="w") as file:
    json.dump(data,file)
print(data)