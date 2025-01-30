Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=True
>>> type(a)
<class 'bool'>
>>> a=10
>>> b=15
>>> c=a>b
>>> c
False
>>> c=a<b
>>> c
True
>>> a={2,3,5,6}
>>> a
{2, 3, 5, 6}
>>> a={"aa","bb","cc","dd"}
>>> a
{'dd', 'bb', 'aa', 'cc'}
>>> a={3,5,7,4,3,7,8,5}
>>> a
{3, 4, 5, 7, 8}
>>> type{a}
SyntaxError: invalid syntax
>>> type(a)
<class 'set'>
>>> a={2,4,6,7}
>>> a
{2, 4, 6, 7}
>>> a.update([10,15])
>>> a
{2, 4, 6, 7, 10, 15}
>>> a.pop()
2
>>> a.remove(6)
>>> a
{4, 7, 10, 15}
>>> a.discard(4)
>>> a
{7, 10, 15}
>>> len(a)
3
>>> a.clear()
>>> a
set()
>>> s="python class"

>>> s="python"
>>> s[1]
'y'
>>> s[0]
'p'
>>> s[-1]
'n'
>>> s[5]
'n'
>>> a="class"
>>> s+a
'pythonclass'
>>> a + s
'classpython'
>>> s+" "+a
'python class'
>>> a=20
>>> s+str(a)
'python20'
>>> s+a
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s+a
TypeError: can only concatenate str (not "int") to str
>>> 3*s
'pythonpythonpython'
>>> s="python"
>>> s[1:4]
'yth'
>>> s[1:2]
'y'
>>> s[-1:-4]
''
>>> s[-4:-1]
'tho'
>>> s[::1]
'python'
>>> s[::-1]
'nohtyp'
>>>
>>>
>>>
>>>
>>> list=[]
>>> type(list)
<class 'list'>
>>> list=[6,7,4,2]
>>> list
[6, 7, 4, 2]

>>> list=[3,3,5,4,5,5,8]
>>> list
[3, 3, 5, 4, 5, 5, 8]
>>> list=["python","class"]
>>> list
['python', 'class']
>>> list[1]
'class'
>>> list[0]
'python'
>>> list=[2,4,"python"]

>>> list
[2, 4, 'python']
>>>
>>>
>>>
>>>
>>> s="python programming is easy"
>>> s.split()
['python', 'programming', 'is', 'easy']
>>> s="python,programe"
>>> s.split(',')
['python', 'programe']
>>> s="python"
>>> list(s)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    list(s)
TypeError: 'list' object is not callable
>>> list(s)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    list(s)
TypeError: 'list' object is not callable
>>> list[s]
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    list[s]
TypeError: list indices must be integers or slices, not str
>>> list[4]
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    list[4]
IndexError: list index out of range
>>> list=[2,4,6,8,65,9]
>>> list[5]
9
>>> list[4]
65
>>> list[2:4]
[6, 8]
>>> list.append(100)
>>> list
[2, 4, 6, 8, 65, 9, 100]
>>> list.insert(2,500)
>>> list
[2, 4, 500, 6, 8, 65, 9, 100]
>>> for i in range(1000,1005):
	list.append(i)
	list
list
SyntaxError: invalid syntax
>>> list.expend([10000,1001,1002])
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    list.expend([10000,1001,1002])
AttributeError: 'list' object has no attribute 'expend'
>>> list=[2,4,6,8,5]
>>> list.extend([1000,1001,1002])
>>> list
[2, 4, 6, 8, 5, 1000, 1001, 1002]
>>> list.remove(5)
>>> list
[2, 4, 6, 8, 1000, 1001, 1002]
>>> list.pop()
1002
>>> list.pop(2)
6
>>> del list[2:5]
>>> list
[2, 4]
>>>
>>>
>>>
>>> dic={}
>>> type(dic)
<class 'dict'>
>>> dic=dict{}
SyntaxError: invalid syntax
>>> dic[1]=1000
>>> dic[2]=2000
>>> dic[3]=3000
>>> dic
{1: 1000, 2: 2000, 3: 3000}
>>> dic={'rollno':'sname':'ABC','marks':300}
SyntaxError: invalid syntax
>>>  dic={'rollno','sname':'ABC','marks':300}

SyntaxError: unexpected indent
>>> dic={'rollno':'sname':'ABC','marks':300}
SyntaxError: invalid syntax
>>> dic={'rollno','sname':'ABC','marks':300}
SyntaxError: invalid syntax
>>> dic={'rollno':101, 'sname': 'ABC', 'marks':300}
>>> dic
{'rollno': 101, 'sname': 'ABC', 'marks': 300}
>>> dic['rollno']
101

>>> dic.get('sname')
'ABC'
>>> dic={1:100,2:200,3:300}
>>> dic.get(1)
100
>>> dic.get(4)
>>> for key in dic:
	print(key)

1
2
3

>>> for key in dic:
	print(dic[key])

100
200
300
>>> for key in dic.values():
	print(key)

100
200
300
>>> dic={1:100,2:200,3:300}
>>> dic2=dic.copy()
>>> dic2
{1: 100, 2: 200, 3: 300}
>>> id(dic)
2348143807936
>>> id(dic2)
2348143824640
>>> len(dic)
3
>>> dic2={6:300,8:200}
>>> dic.update{dic2}
SyntaxError: invalid syntax
>>> dic.update(dic2)
>>> dic
{1: 100, 2: 200, 3: 300, 6: 300, 8: 200}

>>> dic.keys()
dict_keys([1, 2, 3, 6, 8])
>>> dic.values()
dict_values([100, 200, 300, 300, 200])
>>>
