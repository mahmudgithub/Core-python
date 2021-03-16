# # 12.03.2021 pactics 
# name='mahmud hossain'
# print(name)
# # arry in python
# arr=['mahmud','hossain','nannu']
# print(arr[1])
# # add item in arry
# arr.append('lamyaa')
# print(arr)
# # add to arry
# arr2=['bangladersj','pakistan','sodia']
# print(arr+arr2)
# # find method to find any specific item and its location from string
# country='Once upon a time our countruy bangladesh have agood resource of fish ,but recently bangladesh is not enough'
# print(country.find('bangladesh'))
# # use replace method to replace any item in predefined string value
# one=country.replace('bangladesh','islamic')
# print(one)
# # upper case a string
# two='bangladesh'
# print(two.upper())
# # lower case a string
# three='BANGLADESH'
# print(three.lower())
# # split method separate eatch space and show an array list
# print(country.split())
# # count method count repeted string in a full string
# print (country.count('bangladesh'))
# # startwith method check specific starting string and answer true and false
# print(country.startswith('Once'))
# # endwith method ,check specific string at end
# name='mahmud'
# print(name.endwith(d))

# # python dicsonry
# names={'first':'mahmud','second':'hossain'}
# print(names)
# print(names['first'])
# # dicsonry keep a list
# marks={'math':[20,30,40],'english':[60,70,80],'bangla':[10,5,1]}
# print(marks['math'])
# # add new value to dicsonry
# add={'first':'mahmud','second':'hossain'}
# add['third']='nannu'
# print(add)
# # replace value of dicsonry
# add['second']='mahmud'
# print(add)
# # search specific key value from dicspnary
# print('fourth' in add)
# print('first' in add)
# # using get method to found item in dictionary
# print(add.get('five'))
# print (add.get('second'))


# # tuple
# one=('mahmud','hossain','nannu')
# print(one[1])
# # donot update tuple value
# one[1]='mahmud'
# print(one)

# # tuple keep another list,dictionary and tuple to itself
# mix=('mahmud',[1,2,3,4,5],{'second':'hossain'},('a','b','c'))
# print(mix[2])
# # tuple  spered
# a,b,c,d=mix
# print(mix)
# print (a)
# print(b)
# print(c)
# print(d)
# # another way of spred for more tuple element
# more=[1,2,3,4,5,6,7,8,9]
# # a,b,c,*d=more
# # print(a)
# # print(b)
# # print(c)
# # print(d)
# # Or
# a,b,*c,d,e=more
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# # basic input and output functipon
# input ('name:')
# some importace method
# # join method 
# print(','.join(['apple','orange','banana','watermelon']))
# type conversion 
# int to string 
# number=12345
# print(str(number))
# print('i am mahmud '+'my age is '+str(26) + ' i a love to eat')


# # conditionl python
# name='mahmud'
# if name=='mahmudd':print(True)
# else:print(False)
# # # if,else,else-if condition #
# age=int(input('enter age:'))
# if age>18:print('voter age')
# elif age<=18:print('no voter')
# else:print('complex')
# python list
# list=['mango','apple','banana']
# print(list[1])
# # add two list
# list2=['mahmud','hossain','cool']
# print(list+list2)
# print(str(list)*5)
# # check element in list 
# print('mango' in list)
# # check abcence element in list 
# print('mango' not in list)

# # method in python list
# # append method in list
# list=['a','b','c','d','e','f']
# list.append('mahmud')
# print(list)
# # append method add a new list to pre list 
# list.append(['g','h','i'])
# print(list)
# # append add dicsonry to list 
# list.append({'name':'lamyaa','age':19})
# print(list)
# # append method add tuple in list 
# list.append((1,2,3,4,5))
# print(list)
# inset method use on list 
# # insert method add new element in list across index number 
# list =[1,2,3,4]
# list.insert(2,'mahmud')
# print(list)
# # insert tuple,dictionary,and another list to list 
# list.insert(0,('a','b','c'))
# print(list)
# list.insert(0,{'apple','banana'})
# print(list)
# list.insert(0,[5,6,7,8,9])
# print(list)
# index method in list 
# found list elment according to index number 
# list=['a','b','c','d','e']
# print(list.index('d'))
# count method in list 
# # count method count how much element of list are repeted 
# list=[1,2,3,4,5,3,4,5,5,5,6]
# print(list.count(5))
# max method in list 
# # max use to find maximu value of list elment 
# list=[1,2,3,4,5,11111]
# print(max (list))
# # min use to find minimum value of list 
# print(min(list))
# # len use to find length of list 
# print(len(list))
# today pactics 13.3.2021
# python list function 
# # append metthod
# list=[1,2,3,4,5,6]
# print (list)
# list.append('mahmud')
# print(list)
# # inset method in python 
# list.insert(0,'hossain')
# print(list)
# range in python 
# number=list(range(10))
# print(number)
# # create range in specific start and ending
# number=list(range(5,20))
# print(number)
# # create list range with start,step,ending
# number=list(range(5,15,3))
# print(number)
# # for loop in list 
# # lists=[1,2,3,4,5,6,7]
# # for i in lists:
# #     print(i,'mahmud')
# # use range in for loop list 
# # for i in range(10):
# #     print(i)
# # specific range list 
# # for i in range(5,20):
# #     print(i)
# for i in range(5,20,2):
#     print(i)
# # inverse range list for loop 
# for i in range(25,0,-3):
#     print(i)
# # use for loop on string 
# for i in 'python':
#     print(i)
# # use break and cotinue in for loop 
# los=[1,2,3,4,5,6,7,8,9]
# for i in los:
#     if i==5:
#         break;
#     print(i)
# for x in los:
#     if x==5:
#         print('continue:'+str(x))
#         continue;
#     print(x)

# python function 
# def fn():
#     print(' i am first function example of python')
# fn()

# def one(x):
#     return 'i am value of x:'+str(x);
# print(one(10)) 

# # multi prameter handel 
# def multi(*args):
#     for i in args:
#         print(i)

# multi(1,2,3,4,5,6)

# # multi dicsonry handel 
# def multi(**kwargs):
#     print(kwargs)
#     for i in kwargs:
#         print("{0} : {1}".format(i, kwargs[i]))
#         # print(i)
# multi(a=1,b=2,c=3,d=4,e=5)

# # single,double,multi parameter pass to function at a time 
# def both(x,*args,**kwargs):
#     print(x);
#     print(args);
#     print(kwargs)
#     for i in args:
#         print(i);
#     for s in kwargs:
#         print("{0} : {1}".format(s, kwargs[s]))
# both('mahmud',1,2,3,a='hossain',b='nannu',c='mahmud')

# # function return 
# def fn(x,y):
#     return 'sum id:'+str(x+y)
# sos=fn(2,3)
# print(sos)



# single line comment out 
# hello 
# multiline comment out in python
"""
helloffjdjkdjkdjkdjdjddkjdk
djhddddddj
djdddjdjd
"""

# # function assign into variable 
# def one(x):
#     return x;
# two=one
# print(two('mahmud'))

# # function assign to another function as an parameter ,it also said callback function 
# def one(x):
#     return x()
# def two():
#     return 'i am two'
# sos=one(two)
# print(sos)

# # impor module in python 
# import random
# from math import pi,sqrt
# value = random.randint(1, 100)
# print(value)
# print(pi)
# print(sqrt(3))
# # if want to change import module name 
# from math import sqrt as root
# print(root(9))
# # python higher order function 
# def one(fn,x):
#     return fn(x)

# def two(sos):
#     return sos+5

# lol=one(two,10)
# print(lol)

# lamda function in python 
# it also called anonymous function
# lol=(lambda x,y: x+y)(2,2)
# print(lol)
# print((lambda x,y:x-y)(5,2))
# def so(*args): 
#     for x in args:
#         print(x);
# so(1,2,3,4,5)

# # # python map function 
# def one(x):
#     return x*2;
# mark=[1,2,3,4,5]
# result=map(one,mark)
# print(list(result))

# def fn(s):
#     return'hello'+str(s)
# mark=[1,2,3]
# result=map(fn,mark)
# print(list(result))

# # filter method in python
# def one(x):
#     return x%2==0;
# two=[2,3,4,5,6,7,8,9]
# result=filter(one,two)
# print(list(result))
# python decoretor 

# def one(x):
#     print('-------------------------')
#     x()
#     print('-------------------------')

# @one
# def three():
#     print('i am mahmud')
# @one
# def four():
#     print('llllllllllllllllllllllll')

# def one(callback):
#     return callback();
# def two():
#     print('i am callback function')
# one(two)

# @one
# def three():
#     print('i am second callback ')

# # python recursion 
# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return x*factorial(x-1)
# lol=factorial
# print(lol(19))

# # python iteretor tootls 
# from itertools import count
# for i in count(5):
#     print(i)
#     if i>100:
#         break;

# today pactics 16.3.2021 
# class concept in python 
# defined a classical class 
# class one:
#     def fn1():
#         print('i am function one')
# lol=one
# lol.fn1()

# class two:
#     print('hello world')
# j=two

# # constructor or init method 
# class lol:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
# one=lol('mahmud',3)
# print('my name is '+one.name+' my roll is:'+str(one.roll))

# python init method run automatically when another function 
# class one:
#     def __init__(self,names,age):
#         self.names=names
#         self.age=age
#         print('my name is '+names+ 'my age is :'+str(age))
    
#     def two(self):
#         print(' i am from init,my name is :' +str(self.names))

# lol=one('mahmud',26)
# lol.two()

# class lol:
#     def __init__(self):
#         print('i am init function')
#     def one(self):
#         print('i am general function')
# a=lol
# a()
# a.one(a)
# class inheritanc in python 
# class one:
#     def a(self):
#         print('i am function a in class one')
# class two:
#     def b(self):
#         print('i am function b in class two ')
# class three(one,two):
#     def c(self):
#         pass

# lol=three()
# lol.c()