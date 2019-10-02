Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
====================== RESTART: D:\python codes\area.py ======================
>>> 
====================== RESTART: D:\python codes\area.py ======================
>>> convert_2_seconds(5)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    convert_2_seconds(5)
  File "D:\python codes\area.py", line 13, in convert_2_seconds
    seconds=minutes*60
NameError: name 'minutes' is not defined
>>> 
>>> 
====================== RESTART: D:\python codes\area.py ======================
>>> convert_2_seconds(5)
18000
>>> 3<4
True
>>> 3>4
False
>>> 7=7
SyntaxError: can't assign to literal
>>> 7==7
True
>>> 7==7.0
True
>>> x=7
>>> y=8
>>> x<8
True
>>> x==y
False
>>> x!=y
True
>>> grade = 80
>>> grade>+50
True
>>> not(grade>=50)
False
>>> g2
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    g2
NameError: name 'g2' is not defined
>>> 

>>> g2=70
>>> (grade>=50) and (g2>=50)
True
>>> grade=40
>>> (grade>=50) and (g2>=50)
False
>>> g2
70
>>> g2=20
>>> grade=80
>>> (grade>=50) and (g2>=50)
False
>>> (grade>=50) or (g2>=50)
True
>>> grade=40
>>> (grade>=50) and (g2>=50)
False
>>>  three =str(3)
SyntaxError: unexpected indent
>>> three= str(3)
>>> three * 77
'33333333333333333333333333333333333333333333333333333333333333333333333333333'
>>> int(three * 5)
33333
>>> three * 5
'33333'
>>> str(4.65)
'4.65'
]
>>> float('34')
34.0
>>> int('fredsf')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int('fredsf')
ValueError: invalid literal for int() with base 10: 'fredsf'
>>> input("enter a number")
enter a number5
'5'
>>> num_of_shoe=3873
>>> wanted = int(input("shoe"))
shoe54
>>> wanted>num_of_shoe
False
>>> 
