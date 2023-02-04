'''def Happyno(num):

    rem=0
    sum=0
    while(num>0):
       rem=num%10
       sum=sum+(rem*rem)
       num=num//10
    return sum
num=int(input("enter a no:"))
result=num
while(result!=1 and result!=4):
    result=Happyno(result)
if(result==1):
    print("happy no",str(num))
else:
    print("not happy no",str(num))
#oop
#program to create and access an obj
class abc:
    var=10
obj=abc()
print(obj.var)
class abc:
    attribute1=10
obj=abc()
print(obj.attribute1)
class abc:
    attribute1=10
    def display(self):
        print("this is in class")
obj=abc()
print(obj.attribute1)
obj.display()
#creat a constructor in method
class abc:
    def __init__(self,value):
        print("this is in class")
        self.value=value
        print("this value is",value)
obj=abc(100)
class abc:
    class_var=0
    def __init__(self,var):
        abc.class_var +=1
        self.var=var
        print("the obj value is",var)
        print("class value is ",abc.class_var)
obj1=abc(100)
obj2=abc(101)
obj=abc(102)
class Number:
    even=0
    def check(self,num):
        if num%2==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
n=Number()
n.even_odd(21)
class Number:
    even=0
    def check(self,num):
        if num%2==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
n=Number()
n.even_odd(12)
class number:
    even=[]
    odd=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            number.even.append(num)
        else:
            number.odd.append(num)
n1=number(11)
n2=number(12)
n3=number(13)
n4=number(28)
n5=number(7)
print("even number list is", number.even)
            
print("odd number list is", number.odd)'''
 #circle program
class circle:
    pi=3.14159
    def __init__(self,r):
        self.r=r
    def area(self):
        return circle.pi * self.r * self.r
    def circum(self):
        return 2*circle.pi*self.r
c=circle(7.5)
print("area:",c.area())
print("circumference=",c.circum())
