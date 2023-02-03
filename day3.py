Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=9
b=8
print("a=",a)
a= 9
a=6
b=8
a=a+b
b=a-b
a=a-b
SyntaxError: multiple statements found while compiling a single statement
a=a+b
a=a+b
a=a-b
SyntaxError: multiple statements found while compiling a single statement
a=a+b
a=a+b
a=a-b
print("a=",a)
a= 22
print("b=",b)
b= 8
a=9
b=5
print("a=",a)
a= 9
print("b=",b)
b= 5
b= 3
a=a*b
b=a/b
b=a/b
a=a/b
print("a=",a)
a= 9.0
print("b=",b)
b= 3.0
a=5
b=6
print(a)
5
print(b)
6
a=a^b
b=a^b
a=a^b
print(a)
6
print(b)
5
num=[1,2,3,4,5,6,7,8,9,10]
print(num)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("first ele in the list is",num[0])
first ele in the list is 1
print(num[2:5])
[3, 4, 5]
print(num[::2])
[1, 3, 5, 7, 9]
print(num[::1])
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[0])
1
print(num[-5])
6
print(num[-10])
1
print(num[1:3])
[2, 3]
print(num[1::3])
[2, 5, 8]
del num[2:4]
print(num)
[1, 2, 5, 6, 7, 8, 9, 10]
n=[1,'a',"abc",[2,3,4],5.6]
print(n)
[1, 'a', 'abc', [2, 3, 4], 5.6]
print(n[3])
[2, 3, 4]
print(n[3][1])
3
len([1,2,3,4,5])
5
concatination=[1,2]+[3,4]

"gayatri"*10
'gayatrigayatrigayatrigayatrigayatrigayatrigayatrigayatrigayatrigayatri'
'harika'*18
'harikaharikaharikaharikaharikaharikaharikaharikaharikaharikaharikaharikaharikaharikaharikaharikaharikaharika'
x=['a','e']
print(a in x)
False
print(b not in x)
True
num=[1,2,3,6,8]
print(max(num))
8
print(min(num))
1
n=int(input("enter n value:"))
enter n value:10
>>> i=1
>>> while i<=n:
...      s=0
...      s=s+i
...      i+=1
... 
...      
>>> KeyboardInterrupt
>>> print(i)
11
>>> print(s)
10
>>> n=int(input("enter n value:"))
enter n value:10
>>> KeyboardInterrupt
>>> i=1
>>> s=0
>>> while i<=n:
...      s=s+i
...      i+=1
... print(s)
SyntaxError: invalid syntax
>>> print(s)
0
>>> num=[1,2,3,4,5,6,7,8,9,10]
>>>  print(sum(num))
...  
SyntaxError: unexpected indent
>>> num=[1,2,3,4,5,6,7,8,9,10]
>>> print(sum(num))
55
