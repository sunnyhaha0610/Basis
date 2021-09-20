with open("test.txt",mode="w",encoding="utf-8") as file:
    file.write("5\n3")
#讀取檔案
sum=0
with open("test.txt",mode="r",encoding="utf-8") as file:
    for line in file: #一行一行讀取
        sum+=int(line)
print(sum)