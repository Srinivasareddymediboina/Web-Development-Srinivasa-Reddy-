#Collections of variables and
"""class Hi():
	
	a=10
	welcome to all
	b="oop's"
	def Hello():
		print("good morning all")
print(dir(Hi))"""

class Cal():
    """i am creating a calculater app:"""
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
a=int(input("a value"))
b=int(input("b value"))
print("\n 1.add \n 2.sub \n 3.mul \n 4.div")
num=int(input("enter ur choice"))
if num==1:
    print(Cal.add(a,b))
elif num==2:
    print(Cal.sub(a,b))
elif num==3:
    print(Cal.mul(a,b))
elif num==4:
    print(Cal.div(a,b))
    
        
        

    
