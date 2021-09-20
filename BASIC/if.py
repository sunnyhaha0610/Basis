x=int(input("請輸入數字一："))
y=int(input("請輸入數字二："))
s=input("請輸入運算符號：+,-,*,/：")
if s=="+":
    z=x+y
elif s=="-":
    z=x-y
elif s=="*":
    z=x*y
elif s=="/":
    z=x/y
else:
    z="系統不支援此運算"
print(z)

