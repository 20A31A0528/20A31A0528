Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import string
print(string.digits)
0123456789
import stringprint(string.digits)
SyntaxError: invalid syntax
import string
print(string.ascii_letter)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(string.ascii_letter)
AttributeError: module 'string' has no attribute 'ascii_letter'. Did you mean: 'ascii_letters'?
import string
print(string.ascii_letter)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(string.ascii_letter)
AttributeError: module 'string' has no attribute 'ascii_letter'. Did you mean: 'ascii_letters'?
import string
print(string.ascii_letters)
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
import string
ch='g'
print('a' <=ch <='z')
True
str1='hello'
print(dir(str1))
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
#demonstarte match() function
import re
str2='she sells sea shells at sea store
SyntaxError: incomplete input
#demonstarte match() function
import re
str2='she sells sea shells at sea store'
p1='sells'
if re.match(p2,str2):
    print("match found")
else:
    print(p1,"not present in syring")

    
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    if re.match(p2,str2):
NameError: name 'p2' is not defined. Did you mean: 'p1'?
#demonstarte match() function
import re
str2='she sells sea shells at sea store'
p1='sells'
if re.match(p1,st1):
    print("match found")
else:
    print(p1,"not present in string")

    
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    if re.match(p1,st1):
NameError: name 'st1' is not defined. Did you mean: 'str1'?
import re
str2='she sells sea shells at sea store'
p1='sells'
if re.match(p1,str2):
    print("match found")
else:
    print(p1,"not present in string")

    
sells not present in string
p2='she'
if re.match(p2,str2):
    print("match found")
else:
    print(p2,"not present in string")

    
match found

import re
str1='she sells sea shells at sea store'
p1='sea'
rep='ocean'
ns=re.sub(p1,rep,str,1)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    ns=re.sub(p1,rep,str,1)
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python311\Lib\re\__init__.py", line 185, in sub
    return _compile(pattern, flags).sub(repl, string, count)
TypeError: expected string or bytes-like object, got 'type'
ns=re.sub(p1,rep,str1,1)
print(ns)
she sells ocean shells at sea store
import re
p=r'[aeiou]'
if re.search(p,"clue"):
    print("matchy vowel")

    
matchy vowel
ns=re.sub(p1,rep,str1,1)
print(ns)
she sells ocean shells at sea store
import re
p!=r'[aeiou]'
False
if re.search(p,"clue"):
    print("consonants matched")
else:
    print('consonants not matched')

    
consonants matched
str1=listen
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    str1=listen
NameError: name 'listen' is not defined. Did you mean: 'list'?
str1=("listen")
str2=("slient")
m=len(str1)
p=len(str2)
sortstr1==sorted(str1)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    sortstr1==sorted(str1)
NameError: name 'sortstr1' is not defined
sortstr1==sorted(str1)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    sortstr1==sorted(str1)
NameError: name 'sortstr1' is not defined


str1=("listen")
str2=("slient")
m=len(str1)
p=len(str2)
SyntaxError: multiple statements found while compiling a single statement
str1=("listen")
str2=("slient")
m=len(str1)
p=len(str2)
sortstr1=sorted(str1)
sortstr2=sorted(str2)
if m=p:
    
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
if m==p:
    if sortstr1==sortstr2:
        print("anagram")

        
anagram
    else:
        
SyntaxError: unexpected indent
str1=("listen")
str2=("slient")
m=len(str1)
p=len(str2)
sortstr1=sorted(str1)
sortstr2=sorted(str2)
if m==p:
    if sortstr1==sortstr2:
        print("anagram")
    else:
        print("not anagram")
else:
    print("not anagram)
          
SyntaxError: incomplete input
str1=("listen")
          
str1=("listen")
          
str1=("listen")
          
str1=("listen")
          
str1=("listen")
          
str2=("slient")
          
m=len(str1)
          
p=len(str2)
          
sortstr1=sorted(str1)
          
sortstr2=sorted(str2)
          
KeyboardInterrupt
if m==p:
    if sortstr1==sortstr2:
        print("anagram")
     else:
         
SyntaxError: unindent does not match any outer indentation level
val=int(input("enter the val"))
enter the val17
x=0
y=0
for i in range (1,val+1):

    str1=("listen")
str2=("slient")
m=len(str1)
p=len(str2)
sortstr1=sorted(str1)
sortstr2=sorted(str2)
if m==p:
    if sortstr1==sortstr2:
        print("anagram")
    else:
        print("not anagram")
else:
    print("not anagram")
    
SyntaxError: invalid syntax
val=int(input("enter the val"))
enter the val18
x=0
y=0
for i in range (1,val+1):
    if(i%2!=0):
        x=x+2
    else:
        y=y+1
... 
...         
>>> if(val%2!=0):
...     print('{} term in program is{}'.format(val,x-2))
... else:
...     print('{} term in program is{}'.format(val,y-1))
... 
...     
18 term in program is8
>>> str1=("listen")
>>> str2=("slient")
>>> m=len(str1)
>>> p=len(str2)
>>> sortstr1=sorted(str1)
>>> sortstr2=sorted(str2)
>>> if m==p:
...     if sortstr1==sortstr2:
...         print("anagram")
...     else:
...          print("not anagram")
... else:
...      print("not anagram")
... 
...      
anagram
>>> x=int(input("Enter the number"))
Enter the number45
>>> 
>>> 
>>> x=int(input("Enter the number"))
Enter the number6
