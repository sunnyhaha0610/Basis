#set 集合
s1={3,4,5}
print(10 not in s1)
s2={4,5,6,7}
r1=s1&s2 #交集
r2=s1|s2 #聯集
r3=s1-s2 #差集
r4=s1^s2 #反交集
print(r1,"\n",r2,"\n",r3,"\n",r4)
s=set("Hello")
print(s)
print("H" in s)