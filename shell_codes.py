Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 12
>>> b = 22
>>> c = a + b
>>> print(c)
34
>>> type(a)
<class 'int'>
>>> a = "hello"
>>> type(a)
<class 'str'>
>>> 'hello' + 15
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    'hello' + 15
TypeError: can only concatenate str (not "int") to str
>>> 'hello' * 5
'hellohellohellohellohello'
>>> for i in range(1,6) : print('*' * i)

*
**
***
****
*****
>>> a,b = 12,20
>>> a,b = b,a
>>> a
20
>>> b
12
>>> #for i in range(start,stop,step)
>>> for i in range(1,10):
	print(i)
	print("Inside Loop")

	
1
Inside Loop
2
Inside Loop
3
Inside Loop
4
Inside Loop
5
Inside Loop
6
Inside Loop
7
Inside Loop
8
Inside Loop
9
Inside Loop
>>> 
============= RESTART: C:/Users/asus/Desktop/OnlineFDP/code_1.py =============
1
inside loop
2
inside loop
3
inside loop
4
inside loop
5
inside loop
6
inside loop
7
inside loop
8
inside loop
9
inside loop
Outside loop
>>> 
