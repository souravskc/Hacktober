Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> help(abs)
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

>>> 
=============================== RESTART: Shell ===============================
>>> 
====================== RESTART: D:/python codes/tri1.py ======================
>>> help(area)
Help on function area in module __main__:

area(h, b)
    (number,number) ->number
    
    Return the area of triangle with the dimensions given.

>>> area(5,6)
15.0
>>> 
=============================== RESTART: Shell ===============================
>>> 
================== RESTART: D:/python codes/temperature.py ==================
>>>  covert_to_celsius(32)
SyntaxError: unexpected indent
>>> covert_to_celsius(32)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    covert_to_celsius(32)
NameError: name 'covert_to_celsius' is not defined
>>> convert_to_celsius(32)
14.222222222222221
>>> convert_to_celsius(212)
194.22222222222223
>>> 
=============================== RESTART: Shell ===============================
>>> 
================== RESTART: D:/python codes/temperature.py ==================
>>> 
KeyboardInterrupt
>>> convert_to_celsius(32)
0.0
>>> convert_to_celsius(212)
100.0
>>> 
