
def fact(n):
    return 1 if n< 2 else n* fact(n-1)
result= map(fact,range(6))
print(result)
for i in result:
    print(i)
result = list(map(fact,range(6))) #to work z 
for z in result:
    print(z)

#second example of map fun

list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
total= list(map(lambda x,y:x+y,list1,list2))
print(total)

# #generator fun
# def myGen():
#     yield 10
#     yield 30
# result =myGen()
# print(result)
# print(next(result))
# print(result.__next__()) 

from queue import PriorityQueue


# def mySquare():
#     x = 1
#     while x <= 10:
#         square= x * x
#         yield square
#         x+=1
# result=mySquare()
# for i in result:
#     print(i)

# def myGen():
#     value = 10
#     print("first calling")
#     yield value
#     value+=20
#     print("second calling")
#     yield value
#     value+=40
#     print("third calling")
#     yield value
    
# result = myGen()
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())