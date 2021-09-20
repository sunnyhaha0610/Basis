class File:
    def __init__(self,name):
        self.name=name
        self.file=None
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()
f1=File("hahaha.txt")
f1.open()
data1=f1.read()
print(data1)
f2=File("test.txt")
f2.open()
data2=f2.read()
print(data2)