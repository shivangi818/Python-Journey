Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a='Kolkata'
a
'Kolkata'
a="kolkata"
a
'kolkata'
a="""kolkata"""
a
'kolkata'
a='''kolkata'''
a
'kolkata'
>>> city="kolkata"
>>> city[0]
'k'
>>> city[1]
'o'
>>> city[-1]
'a'
>>> city[-4]
'k'
>>> #indexing
>>> #positive
>>> #1
>>> #left to right
>>> 
>>> #negative
>>> #-1
>>> #right to left
>>> 
>>> city
'kolkata'
>>> city[1:4]
'olk'
>>> city[-3:-1]
'at'
>>> city[-2:]
'ta'
>>> city[1:]
'olkata'
>>> city[:-3]
'kolk'
>>> city[1:5:2]
'ok'
>>> city[0]='X'
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    city[0]='X'
TypeError: 'str' object does not support item assignment
>>> #strings in python are immutable
>>> #strings in python are immutable
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #strings in python are immutable
>>> 
>>> city[-3]='ooo'
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    city[-3]='ooo'
TypeError: 'str' object does not support item assignment
>>> city='Mumbai'



del city
city
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    city
NameError: name 'city' is not defined
city="kokata"
del city[0]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    del city[0]
TypeError: 'str' object doesn't support item deletion
city*3
'kokatakokatakokata'
city2="mumbai"
city+city2
'kokatamumbai'
#String concatenation

city-city2
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    city-city2
TypeError: unsupported operand type(s) for -: 'str' and 'str'
city**3
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    city**3
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
city>city2
False
city>=city2
False
city<city2
True
#lexiography


for i in "goa"
SyntaxError: incomplete input
for i in "goa":
    print(i)

    
g
o
a
print(i)
a
[g,o,a]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    [g,o,a]
NameError: name 'g' is not defined

"Del" in "Delhi"
True
"Del" not in "New Delhi"
False
"India is a {} country. Its capital is {}".format("great","Delhi")
'India is a great country. Its capital is Delhi'
"India is a {1} country. Its capital is {0}".format("great","Delhi")
'India is a Delhi country. Its capital is great'
len("Hello World")
11
len(city)
6
city="Kolkata"
min(city)
'K'
max(city)
't'
#ASCII Value
#A=65
B=66
#a=97
#B=66
sorted("Kolkata")
['K', 'a', 'a', 'k', 'l', 'o', 't']
sorted("Kolkata", reverse=True)
['t', 'o', 'l', 'k', 'a', 'a', 'K']
"Kolkata".upper()
'KOLKATA'
"kolkata".lower()
'kolkata'
"hello WorLd".capitalize()
'Hello world'
city="kolkata"
city=7
"It rained heavily in Haldia".split()
['It', 'rained', 'heavily', 'in', 'Haldia']
