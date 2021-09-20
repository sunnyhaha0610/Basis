n=int(input("請輸入一個正整數："))
for i in range(n):
    if i*i==n:
        print("整數平方根：",i)
        break
else:
    print("無整數平方根")
    