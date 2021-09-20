student=["Amy","John","Kris","Jenny"]
score=[59,80,44,91]
for i in range(4):
    print(student[i]+"的分數為：",score[i])
    if score[i]>=60:
        continue
    print(student[i]+"通過")