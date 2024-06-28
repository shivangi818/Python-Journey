Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
L1=[1,2,3,4]
L1
[1, 2, 3, 4]
type(L1)
<class 'list'>
#how to create
L1
[1, 2, 3, 4]
#Homogeneous list
L2=[1,"hello",6]
L2
[1, 'hello', 6]
#Heterogeneous



#Compound data types
L3=[]
L3
[]
#Empty List

L4=[1,3,2,[1,4]]
L4
[1, 3, 2, [1, 4]]
#Multi d List
#2Dlist
L5=[[1,2],[3,4],5,6,]
L5
[[1, 2], [3, 4], 5, 6]
str(7)
'7'
int(7)
7
L6=list("Goa")
L6
['G', 'o', 'a']


L1
[1, 2, 3, 4]
L1[0]
1
l1[6]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    l1[6]
NameError: name 'l1' is not defined. Did you mean: 'L1'?
L1[6]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    L1[6]
IndexError: list index out of range
L1[2:5]
[3, 4]
L1[-4:-1]
[1, 2, 3]
L1[0]=1000
L1
[1000, 2, 3, 4]
L1[-1]=67
L1
[1000, 2, 3, 67]


L1.append("Haldia")
L1
[1000, 2, 3, 67, 'Haldia']
L1.extend([1,2,3])
L1
[1000, 2, 3, 67, 'Haldia', 1, 2, 3]
\
L1.extend("Goa")
L1
[1000, 2, 3, 67, 'Haldia', 1, 2, 3, 'G', 'o', 'a']
L1.append([1,2,3])
L1
[1000, 2, 3, 67, 'Haldia', 1, 2, 3, 'G', 'o', 'a', [1, 2, 3]]
L1.insert(1,Kolkata)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    L1.insert(1,Kolkata)
NameError: name 'Kolkata' is not defined
Li.insert(1,"Kolkata")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    Li.insert(1,"Kolkata")
NameError: name 'Li' is not defined. Did you mean: 'L1'?
L1.insert(1,"Kolkata")

L1
[1000, 'Kolkata', 2, 3, 67, 'Haldia', 1, 2, 3, 'G', 'o', 'a', [1, 2, 3]]
del L1[0]
L1
['Kolkata', 2, 3, 67, 'Haldia', 1, 2, 3, 'G', 'o', 'a', [1, 2, 3]]
del L1[-1]
L1
['Kolkata', 2, 3, 67, 'Haldia', 1, 2, 3, 'G', 'o', 'a']
del L1[-3:,-1]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    del L1[-3:,-1]
TypeError: list indices must be integers or slices, not tuple
del L1[-3:]
L1
['Kolkata', 2, 3, 67, 'Haldia', 1, 2, 3]
L3
[]
del L3
L3
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    L3
NameError: name 'L3' is not defined. Did you mean: 'L1'?
del L3[]
SyntaxError: incomplete input
L
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    L
NameError: name 'L' is not defined. Did you mean: 'L1'?
L1.remove("Kolkata")
L1
[2, 3, 67, 'Haldia', 1, 2, 3]
L1.remove("hehe")
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    L1.remove("hehe")
ValueError: list.remove(x): x not in list
L1.pop()
3
L1.pop()
2
L1
[2, 3, 67, 'Haldia', 1]
L1.clear()
L1
[]
L1=[1,2,3,4,5]
L1*2
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
L1+2
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    L1+2
TypeError: can only concatenate list (not "int") to list
L1
[1, 2, 3, 4, 5]
L2=["jiii",3,4]
L1+L2
[1, 2, 3, 4, 5, 'jiii', 3, 4]
"Kol" in "Kolkata"
True
L1
[1, 2, 3, 4, 5]
4 in L1
True
7 in l1
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    7 in l1
NameError: name 'l1' is not defined. Did you mean: 'L1'?
7 in L1
False
L4
[1, 3, 2, [1, 4]]
[1,4] in L5
False


L4
[1, 3, 2, [1, 4]]
L4[2]
2
L4=[1,2,3,[4,5]]
L4
[1, 2, 3, [4, 5]]
L4[2]
3
L4[3]
[4, 5]
x=L4[3]
x
[4, 5]
x[1]
5
L4[3][1]
5
L5 =[[[1,2],[3,4]],[[5,6],[7,8]]]
L5
[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
L5[2]
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    L5[2]
IndexError: list index out of range
L5[1]
[[5, 6], [7, 8]]
x=L5[1]
x
[[5, 6], [7, 8]]
x[1]
[7, 8]
x[0]
[5, 6]
y=x[0]
y
[5, 6]
y[0]
5
y[1]
6
L5[1][0][1]
6
L5
[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
L5[0][1][0]
3
for i in "kolkata"
SyntaxError: incomplete input
for i in "L1"
SyntaxError: incomplete input
for i in L1
SyntaxError: incomplete input
for i in L1:
    print(i)

    
1
2
3
4
5
for i in L4:
    print(i)

    
1
2
3
[4, 5]
L1
[1, 2, 3, 4, 5]
len(L1)
5
min(L1)
1
max(L1)
5
L1=[3,2,4,1,5,6]
sorted(L1)
[1, 2, 3, 4, 5, 6]
sorted(L1,reverse=True)
[6, 5, 4, 3, 2, 1]
L1
[3, 2, 4, 1, 5, 6]
>>> L1.sort()
>>> L1
[1, 2, 3, 4, 5, 6]
>>> L1=1,2,3,4,5
>>> x=sorted(L1)
>>> L1
(1, 2, 3, 4, 5)
>>> L1=[3,2,4,1,5,6]
>>> x=sorted(L1)
>>> L1
[3, 2, 4, 1, 5, 6]
>>> x
[1, 2, 3, 4, 5, 6]
>>> x=L1.sort()
>>> x
>>> 
>>> L1
[1, 2, 3, 4, 5, 6]
>>> x
>>> x
>>> y=None
>>> y
>>> y
