Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a,b,c=10,20,30
print(b,c,a)
20 30 10
print(b,c,a,sep='?')
20?30?10
print('09','12','2016', sep='-')
09-12-2016
print('A','B','C',SEP='-')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print('A','B','C',SEP='-')
TypeError: 'SEP' is an invalid keyword argument for print()
print('A','B','C',sep='-')
A-B-C
apple=100
banana=200
pineapple=300
print(banana)
SyntaxError: multiple statements found while compiling a single statement
apple=100
banana=200
pineapple=300
print(banana)
200
print(apple)
100
print(apple,banana,pineapple)
100 200 300
print(apple,end=' ')
100 
print(banana,end=' ')
200 
x,y,z=input("enter a three values: ").split()
enter a three values: 100
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x,y,z=input("enter a three values: ").split()
ValueError: not enough values to unpack (expected 3, got 1)
x,y,z=input("enter a three values: ").split()
enter a three values: 100 700 600
print("total no of students: ",x)
total no of students:  100
print("no of boys: ",y)
no of boys:  700
print("no of girls: ",y)
no of girls:  700
x,y,z=input("enter a three values: ").split('&')
enter a three values: 1000 2000 * 3000 - 4000 & 5000 6000 ( 7000 + 8000 & 90000
print("total no of students: ",x)
                                                            
total no of students:  1000 2000 * 3000 - 4000 
print("no of boys: ",y)
                                                            
no of boys:   5000 6000 ( 7000 + 8000 
print("no of girls: ",z)
                          
no of girls:   90000
x,y,z=input("enter a three values: ").split('0')
                          
enter a three values: 67
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    x,y,z=input("enter a three values: ").split('0')
ValueError: not enough values to unpack (expected 3, got 1)
x,y,z=input("enter a three values: ").split('0')
                          
enter a three values: 100
print("total no of students: ",x)
                          
total no of students:  1
print("no of boys: ",y)
                          
no of boys:  
print("no of girls: ",z)
                          
no of girls:  
x,y,z=input("enter a three values: ").split('0')
                          
enter a three values: 20304
print("total no of students: ",x)
                          
total no of students:  2
print("no of boys: ",y)
                          
no of boys:  3
print("no of girls: ",z)
                          
no of girls:  4
CONTROL STATEMENTS
                          
SyntaxError: incomplete input
email="harikachitturi23@gmail.com"
                          
pwd=123456
                          
cemail=input("enter the email:")
                          
enter the email:sainaveen@gmail.com
cpwd=input("enter the email:")
                          
enter the email:123456
if(email==cemail and pwd==cpwd):
    print("login successfull")
else:
     print("login unsuccessfull")

     
login unsuccessfull
email="harikachitturi23@gmail.com"
cemail=input("enter the email:")
enter the email:harikachitturi23@gmail.com
cpwd=int(input("enter the email:"))
enter the email:harikachitturi23@gmail.com
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    cpwd=int(input("enter the email:"))
ValueError: invalid literal for int() with base 10: 'harikachitturi23@gmail.com'
cpwd=int(input("enter the email:"))
enter the email:123456
if(email==cemail and pwd==cpwd):
    print("login successfull")
else:
    print("login unsuccessfull")

login successfull
email="gayatri@gmail.com"
pwd=123456
cemail=input("enter the email:")
enter the email:gayatri@gmail.com
cpwd=int(input("enter the pwd:"))
enter the pwd:123456
if(email==cemail and pwd==cpwd):
    print("login successful")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to mail")
elif(email==cemail and pwd!=cpwd):
    print("login failed due to pwd")
elif(email!=cemail and pwd!=cpwd):
    print("login failed due to mail and pwd")
    
SyntaxError: multiple statements found while compiling a single statement
email="gayatri@gmail.com"
pwd=123456
cemail=input("enter the email:")
enter the email:gayatri@gmail.com
cpwd=int(input("enter the pwd:"))
enter the pwd:
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    cpwd=int(input("enter the pwd:"))
ValueError: invalid literal for int() with base 10: ''
if(email==cemail and pwd==cpwd):
    print("login successful")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to mail")
elif(email==cemail and pwd!=cpwd):
    print("login failed due to pwd")
elif(email!=cemail and pwd!=cpwd):
    print("login failed due to mail and pwd")

    
login successful
email="harikachitturi23@gmail.com"
pwd=123456
cemail=input("enter the email:")
enter the email:harikachitturi23@gmail.com
pwd=123456
cpwd=int(input("enter the pwd:"))
enter the pwd:123456
if(email==cemail and pwd==cpwd):
    print("login successful")

    
login successful
email="harikachitturi23@gmail.com"
pwd=123456
cemail=input("enter the email:")
enter the email:harikachitturi23@gmail.com
cpwd=int(input("enter the pwd:"))
enter the pwd:123456
otp=1256
if(email==cemail and pwd==cpwd):
    cotp=int(input("enter otp:"))

    
enter otp:1234
if(cotp=int(input("enter otp:"))):
    
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
   if(cotp=int(input("enter otp:"))):
       
SyntaxError: unexpected indent
email="harikachitturi23@gmail.com"
KeyboardInterrupt
pwd=123456
cemail=input("enter the email:")
enter the email:harikachitturi23@gmail.com
cpwd=int(input("enter the pwd:"))
enter the pwd:123456
otp=1256
if(email==cemail and pwd==cpwd):
    cotp=int(input("enter otp:"))

    
enter otp:1234
if(email==cemail and pwd==cpwd):
    cotp=int(input("enter otp:"))
    if(cotp==otp):
        print("order successfull")
    else:
        print("order unsuccessfull")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to mail")

enter otp:1234
order unsuccessfull
a="Harika"
print('y' not in a)
True
print('y' in a)
False
print(a[3])
i
for i in range(1,10):
    print(i)

    
1
2
3
4
5
6
7
8
9
days=int(input("enter no of days:"))
enter no of days:15
calls=int(input("enter no of calls:"))
enter no of calls:250
msg=int(input("enter no of msg:"))
enter no of msg:95
data=float(input("enter data:"))
enter data:1.7
if days<=84:
...     print("remaining days:",84-days)
...     print("remaining calls:",3000-calls)if calls<=3000 else print("calls not connected")
... 
remaining days: 69
remaining calls: 2750
>>> KeyboardInterrupt
>>> print("remaining msg:",100-msg)if msg<=100 else print("message failed")
remaining msg: 5
>>> print("remaining data:",2-data)if data<=2 else print("data completed")
remaining data: 0.30000000000000004
>>> else:
...     
SyntaxError: invalid syntax
>>> if days<=84:
...     print("remaining days:",84-days)
...     print("remaining calls:",3000-calls)if calls<=3000 else print("calls not connected")
...     print("remaining msg:",100-msg)if msg<=100 else print("message failed")
...     print("remaining data:",2-data)if data<=2 else print("data completed")
... else:
...     print("your plan expired")
... 
...     
remaining days: 69
remaining calls: 2750
remaining msg: 5
remaining data: 0.30000000000000004
>>> for i in range(1,151):
...     if(i%10==0):
...         print(i)
... 
...         
10
20
30
40
50
60
70
80
90
100
110
120
130
140
150
for i in range(1,6,2):
    print(i*5)

    
5
15
25
for i in range(1,30):
    if(i%2==1 and i<=5):
        print(i*5)

        
5
15
25
