# # basic function declaration 
# def fun():
#     print('i am first function')
# fun()




# # argument functoion 
# def fun1(x,y):
#     print((x+y))
# fun1(2,2)




# # arbitary argument function ,in javasctript its call rest parameter
# def fun2(*args):
#     print(args)
# fun2(1,2,3,4,5)



# # keyword argument function
# def fun3(x,y,z):
#     print(x)
#     print(y)
#     print(z)
# fun3(x='mahmud',y='hossain',z='nannu')


# Arbitrary Keyword Arguments, **kwargs 
# def fun4(**kwargs):
#     print(kwargs)
# fun4(a='mahmud',b='hossain')


# Default Parameter Value 
def fn5(y,z,x='mamud'):
   
    print(y)
    print(z)
    print(x)
fn5(1,2)