Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=4
... b=8
... c=9
... if(a>b & a>c):
...     if(b>c):
...         print(a,b,c)
...     else:
...         print(a,c,b)
... elif(b>c & b>a):
...     if(c>a):
...         print(b,c,a)
...     else:
...         print(b,a,c)
... elif(a>b):
...     print(c,a,b)
... else:
...     print(c,a,b)Enter "help" below or click "Help" above for more information.
...     
SyntaxError: multiple statements found while compiling a single statement
>>> if(a>b and a>c):
...     if(b>c):
...         print(a,b,c)
...     else:
...         print(a,c,b)
... elif(b>c and b>a):
...     if(c>a):
...         print(b,c,a)
...     else:
...         print(b,a,c)
... elif(a>b):
...     print(c,a,b)
... else:
...     print(c,a,b)
... 
...     
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    if(a>b and a>c):
NameError: name 'a' is not defined

>>> 
>>> 
>>> 
>>> 
>>> 
