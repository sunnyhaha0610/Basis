#dictionary 
dic1={"cat":"貓","dog":"狗"}
print(dic1)
print(dic1["cat"])
dic1["cat"]="貓咪"
print(dic1["cat"])
print("pig" in dic1)
del dic1["dog"]
print(dic1)
s={5,8,9}
dic2={x:x**2 for x in s}
print(dic2)