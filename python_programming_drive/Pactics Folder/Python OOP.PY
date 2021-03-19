# Today 19.03.2021
# topics :python object oriented programming 
# studay links: https://codeloop.org/python-object-oriented-programming-oop/#more-580 
# create a class in python 
class Person:
    def __init__(self):
        print('i am first class example of python class ')
lol=Person()
lol

# add parametrs to class 
class Person:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city

        print('my name is '+name+'my age is '+str(age)+' my city is ' +city)
one=Person('mahmd',25,'rajshahi')
one
two=Person('hossain',22,'pabna')
two
