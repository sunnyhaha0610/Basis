#List 有序可動列表
grades=[12,60,45,70,90]
print(grades)
print(grades[1:4])
grades[0]=55
print(grades)
grades=grades+[25,59]
print(grades)
print(len(grades))
grades[1:4]=[]
print(grades)
#巢狀列表
data=[[3,4,5],[6,7,8]]
print(data)
print(data[0][:2])
data[0][0:2]=[5,5,5]
print(data)
