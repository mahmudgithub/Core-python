# Today 19.03.2021
# topics :python object oriented programming 
# studay links: https://codeloop.org/python-object-oriented-programming-oop/#more-580 
# # create a class in python 
# class Person:
#     def __init__(self):
#         print('i am first class example of python class ')
# lol=Person()
# lol

# # add parametrs to class 
# class Person:
#     def __init__(self,name,age,city):
#         self.name=name
#         self.age=age
#         self.city=city

#         print('my name is '+name+'my age is '+str(age)+' my city is ' +city)
# one=Person('mahmd',25,'rajshahi')
# one
# two=Person('hossain',22,'pabna')
# two

# # define method in class 
# class one:
#     def __init__(self,name,city):
#         self.name=name
#         self.city=city
#     def fn(self):
#         print('i am '+self.name+'my city is '+self.city)

# lol=one('mahmud','rajshahi')
# lol.fn()

# different propertics of python class
# encapsulation propertics 
#this preventing data from direct modification,  
# in python we denote the private attributes by using single _ or double __
# class encapsulation:
#     def __init__(self):
#         pass
#     def one(self):
#         print('i am function one')
#     # def _two(self):
#     #     print('i am function two ')
#     # def __three(self):
#     #     print('i am function three')
# lol=encapsulation()
# lol.one()  #function one is accesseable cause it is public
# # lol.two() # function two is privet 
# # lol.three() #function two is not accessable cause it is privet

# inheritance propertics of python 
# class one:
#     def fn1(self):
#         print('i am function one')
# class two:
#     def fn2(self):
#         print('i am function two')
# class three(one,two):
#     pass

# lol=three()
# lol.fn2()
# classification of inheritance 

# multiple iheritance
# If a class inherits more than one class we can call it multiple
# inheritances.
# class one:
#     def fn1(self):
#         print(' i am first function of class one')
# class two(one):
#     def fn2(self):
#         print('i am function two from class two ')
# class three(one,two):
#     def fn3(self):
#         print('i am function thre of class three')

# lol=three()
# lol.fn3()

# multilavel inheritance 
# class one:
#     def fn1(self):
#         print(' i am first function of class one')
# class two(one):
#     def fn2(self):
#         print('i am function two from class two ')
# class three(two):
#     def fn3(self):
#         print('i am function thre of class three')

# lol=three()
# lol.fn3()

# # hirarchical inheritance 
# class one:
#     def fn1(self,name):
#         self.name=name
#         print(self.name + ' is running')
# class two(one):
#     def fn2(self,name):
#         self.name=name
#         peint('hello world')
# class three(one):
#     pass

# lol=two()
# lol.fn1('mahmud')
# # lol.fn2()

# sos=three()
# sos.fn1('hossain')

# python overriding 
class one:
    def fn1(self):
        print('i am fn one of class one')
class two(one):
    def fn1(self):
        print('i am fn2 of class two')

lol=two()
lol.fn1()