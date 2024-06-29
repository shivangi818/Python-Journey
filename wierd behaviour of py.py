Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="Harry Potter"
>>> b=a
>>> c=b
>>> del a
>>> del b
>>> del c
>>> a=4
>>> b=4
>>> 
>>> 
>>> id(a)
140711443620744
>>> id(b)
140711443620744
>>> a=256
>>> b=256
>>> id(a)
140711443628808
>>> id(b)
140711443628808
>>> a=25
>>> a=4
>>> b=4
>>> id(a)
140711443620744
>>> id(b)
140711443620744
>>> a=257
>>> b=257
>>> id(a)
2932192099856
>>> id(b)
2932192099824
>>> a=-5
>>> b=-5
>>> id(a)
140711443620456
>>> id(b)
140711443620456
>>> a=-6
>>> b=-6
>>> id(a)
2932192095760
>>> id(b)
2932192099856
>>> 

>>> a="haldia"
>>> b="haldia"
>>> a is b
True
