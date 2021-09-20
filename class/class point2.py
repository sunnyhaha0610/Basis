class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x,self.y)
    def distance(self,targetx,targety):
        return(((self.x-targetx)**2)+((self.y-targety)**2))**0.5
p=Point(3,4)
p.show()
result=p.distance(0,0)
print(result)
