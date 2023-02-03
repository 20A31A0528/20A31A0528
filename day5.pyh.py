'''def total(a,b):
    result=a+b
    print("function result is",result)
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
total(a,b)'''
'''def total(a,b):
    res1=a+b
    print("function result is",res1)
def sub(a,b):
    res2=a-b
    print("function result is",res2)
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
total(a,b)
sub(a,b)'''
'''def total(a,b):
    res1=a+b
    print("function result is",res1)
def sub(a,b):
    res2=a-b
    print("function result is",res2)
def mul(a,b):
    res3=a*b
    print("function result is",res3)
def div(a,b):
    res4=a/b
    print("function result is",res4)
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
total(a,b)
sub(a,b)
mul(a,b)
div(a,b)'''
'''def hn(money):
    print("give hn the sum of",money)
money=50
hn(money)'''
'''def hn(money):
     print("given hn the sum of", money)
hn(5*10)'''
'''var = 'harika'
def show():
    global var1
    var1 ='tall'
    print("in function var is",var)
show()
print("outside fun tall",var1)
print("variable is var",var)'''
'''def outf():
     var=10
     def innf():
         var=20
         print("inner var",var)
     innf()
     print("outer var", var)
outf()'''
'''def cube(x):
    
    print("the result is",res)
x=int (input("enter a no:"))
cube(x)
def cube(x):
    return(x*x*x)
num=8
result= cube(num)
print("output of the evaluation is ", result)
def total(a,b,c,d,e,f):
    return(a+b+c+d+e+f)
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
d=int(input("Enter a number"))
e=int(input("Enter a number"))
f=int(input("Enter a number"))
y=total(a,b,c,d,e,f)
print('the sum of 6no',y)
def display(str1):
    print(str1)
str1='hello'
display(str1)
def display(name,age):
    print("name",name)
    print("age",age)
n="hn"
y=99
display(name=n,age=y)'''
def fib(n):
    if n<2:
        return 1
    return(fib(n-1)+(n-2))
n=int(input())
for i in range(n):
    print("fibonacci(",i,")",fib(i))
    
