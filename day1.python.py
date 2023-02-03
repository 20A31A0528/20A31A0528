Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(chr(3129)+chr(3120)+chr(3135)+chr(3093))
హరిక
>>> x,y,z="apple","bannana","pineapple"
>>> print(x)
apple
>>> print(y)
bannana
>>> print(z)
pineapple
>>> print(x+y)
applebannana
>>> print(x,y)
apple bannana
>>> x="How are u"
>>> y="fine"
>>> print(x+y)
How are ufine
>>> print(x,y)
How are u fine
>>> name=int(input("Enter your name"))
Enter your nameHarika
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    name=int(input("Enter your name"))
ValueError: invalid literal for int() with base 10: 'Harika'
>>> name=int(input("Enter your name"))
Enter your nameharika
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    name=int(input("Enter your name"))
ValueError: invalid literal for int() with base 10: 'harika'
name=int(input("Enter your name"))
Enter your name
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    name=int(input("Enter your name"))
ValueError: invalid literal for int() with base 10: ''

name=int(input("Enter your name:"))
Enter your name:harika
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    name=int(input("Enter your name:"))
ValueError: invalid literal for int() with base 10: 'harika'
name=input("Enter your name")
Enter your name harika
age=input("Enter your age")
Enter your age20
salary=float("Enter your salary")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    salary=float("Enter your salary")
ValueError: could not convert string to float: 'Enter your salary'
salary=input("Enter your salary")
Enter your salary7.5
print(name,age)
 harika 20
print(name,age,salary)
 harika 20 7.5
a=input("Enter a")
Enter a5
b=input("Enter b")
Enter b6
print(a+b)
56
print(a//b)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(a//b)
TypeError: unsupported operand type(s) for //: 'str' and 'str'
KeyboardInterrupt
print(a/b)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(a/b)
TypeError: unsupported operand type(s) for /: 'str' and 'str'
c=a//b
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    c=a//b
TypeError: unsupported operand type(s) for //: 'str' and 'str'
print(a//b)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(a//b)
TypeError: unsupported operand type(s) for //: 'str' and 'str'
a=input("Enter a")
Enter a6
b=input("Enter b")
Enter b8
c=a/b
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    c=a/b
TypeError: unsupported operand type(s) for /: 'str' and 'str'
a=input("Enter a")
Enter a

a=int(input("Enter a"))
Enter a7
b=int(input("Enter b"))
Enter b9
c=a//b
d=a**b
e=a/b
print(c,d,e)
0 40353607 0.7777777777777778
x=6
y=7
print(x+y)
13
print(x-y)
-1
print(x/y)
0.8571428571428571
print(x%y)
6
print(x//y)
0
 print(x*y)
 
SyntaxError: unexpected indent
print(x*y)
42
x=9
y=8
print(x<y)
False
print(x>y)
True
print(x=)
SyntaxError: incomplete input
print(x=y)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    print(x=y)
TypeError: 'x' is an invalid keyword argument for print()
print(x==y)
False
print(x<=y)
False
print(y>=x)
False
a=2
b=5
a=5
print(a+)
SyntaxError: incomplete input
a=5
print(a+=7)
SyntaxError: invalid syntax
(a+=10)
SyntaxError: invalid syntax
a=5
b=8
c=a&b
d=a^b
e=a*b
f=~a
g=~(a^b)
print(a)
5
print(b)
8
print(c)
0
print(d)
13
print(e)
40
print(f)
-6
print(g)
-14
a=1000
b=1500
c=-500
d=4000
e=2000
print(a<b and a<c)
False
print(a>b or a>b)
False
print(a>b and a>c and a>d)
False
print(a if(a>b and a>c and a>d and a>e and a>e)else b if(
KeyboardInterrupt
print(a if(a>b and a>c and a>d and a>e)else b if(b>c and b>d and b>e )else c if(c>d and c>e) else d if(d>e)else e)
4000
