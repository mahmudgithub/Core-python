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

# class A:
#     def a_method(self):
#         print("A method from class A")


# class B:
#     def b_method(self):
#         print("B method from Class B")


# class C(A,B):
#     pass


# c = C()
# c.a_method()
# c.b_method()

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

# # python overriding 
# class one:
#     def fn1(self):
#         print('i am fn one of class one')
# class two(one):
#     def fn1(self):
#         print('i am fn2 of class two')

# pol=one()
# pol.fn1()
# lol=two()
# lol.fn1()


# class Animal:
#     def run(self, name):
#         self.name = name
#         print(f'{self.name} Is Runing')



# class Dog(Animal):
#     pass



# class Cat(Animal):
#     pass



# dog = Dog()
# dog.run("Dog")


# cat = Cat()
# cat.run("Cat")

# # super/init function in python 
# class one:
#     def __init__(self):
#         print('i am first init function')

# class two(one):
#     def __init__(Self,name):
#         print('i am second init function,and my name is :'+name)
# lol=one()
# sos=two('mahmud')

# class one:
#     def __init__(Self):
#         print('i am first init method')
# class two:
#     def __init__(self):
#         print('i am second init method')

# class three:
#     def __init__(self):
#         print('i am third init method')
# class four(one,three):
#     def __init__(self):
#         super().__init__()
#         print('i am all fun')
# lol=four()

# class one:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# class two(one):
#     def __init__(self,name,age,city):
#         super().__init__(name,age)
#         self.city=city
#         print('i am :'+name+'my age :'+age+'my city :'+city)

# lol=two('mahmud','26','rajshahi')

# class one:
#     def __init__(self,name):
#         self.name=name

# class two:
#     def __init__(self,age):
#         self.age=age

# class three(one,two):
#     def __init__(self,name,age,city):
#         self.city=city
#         print('i am :'+name+' my age is :'+age+' my city is :'+city)
# lol=three('mahmud','26','raj')


