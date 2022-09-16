def myFun(fn,*args,**kwargs):#higher order fun
    return fn(*args,**kwargs) 

result = myFun(lambda x,y: x+y,3,5)
print(result)

def data(fn,*args,**kwargs):
    return fn(*args,**kwargs)
result = data(lambda x,*,y: x+y, 10, y=20)#bcoz of end of position, add y=20
value = data(lambda *args: sum(args),1,2,3,4,5)
print(result)
print(value)