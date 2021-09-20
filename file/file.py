#儲存檔案
#(一)
file1=open("data1.txt",mode="w",encoding="utf-8") #開啟
file1.write("哈囉\n測試") #操作
file1.close() #關閉
#(二)
with open("data2.txt",mode="w") as file2:
    file2.write("Hello\nTest")
