#fullname實體物件：分開紀錄姓、名資料的全名
class Fullname:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name1=Fullname("S.S.","Huang")
print(name1.first,name1.last)
name2=Fullname("Y.W.","Huang")
print(name2.first,name2.last)