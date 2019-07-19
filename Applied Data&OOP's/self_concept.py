class cal():
    def __init__(self,a,b):
        self.n1=a
        self.n2=b
        #print(self.n1,self.n2)
    def display(self):
        print(self.n1,self.n2)
    def add(self):
        return self.n1+self.n2
    def sub(self):
        return self.n1-self.n2
    def mul(self):
        return self.n1*self.n2
    def div(self):
        return self.n1/self.n2
a=int(input("a value"))
b=int(input("b value"))
obj=cal(a,b)
obj.display()
print(obj.add())
print(obj.sub())
print(obj.mul())
print(obj.div())
