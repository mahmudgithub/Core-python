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
class one:
    def fn1(self):
        print('i am function one')
class two:
    def fn2(self):
        print('i am function two')
class three(one,two):
    pass

lol=three()
lol.fn2()
