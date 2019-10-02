Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> max(389,13278)
13278
>>> max(3,321,132,234)
321
>>> dir(_builtins_)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    dir(_builtins_)
NameError: name '_builtins_' is not defined
>>> dir(__uiltins__)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    dir(__uiltins__)
NameError: name '__uiltins__' is not defined
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> help(max)
Help on built-in function max in module builtins:

max(...)
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.

>>> help(abs)
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.

>>> abs(-5465.4)
5465.4
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> help(pow)
Help on built-in function pow in module builtins:

pow(x, y, z=None, /)
    Equivalent to x**y (with two arguments) or x**y % z (with three arguments)
    
    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

>>> pow(2,5)
32
>>> def f(x):
	return x**2

>>> f(3)
9
>>> area
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    area
NameError: name 'area' is not defined
>>> result =f(3)
>>> resultr
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    resultr
NameError: name 'resultr' is not defined
>>> result
9
>>> def area(base,height):
	return base* height /2

>>> area(3,4)
6.0
>>> area(32,4.45)
71.2
>>> 
=============================== RESTART: Shell ===============================
>>> area(12,21)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    area(12,21)
NameError: name 'area' is not defined
>>> area(421,432)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    area(421,432)
NameError: name 'area' is not defined
>>> 
 RESTART: C:/Users/Gabbar Hacker/AppData/Local/Programs/Python/Python37-32/triangle.py 
>>> area(21,123)
1291.5
>>> 
 RESTART: C:/Users/Gabbar Hacker/AppData/Local/Programs/Python/Python37-32/triangle.py 
>>> perimeter(4,5,6)
15
>>> 
=============================== RESTART: Shell ===============================
>>> area
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    area
NameError: name 'area' is not defined
>>> 
 RESTART: C:/Users/Gabbar Hacker/AppData/Local/Programs/Python/Python37-32/triangle.py 
>>> area(1,2)
1.0
>>> 
