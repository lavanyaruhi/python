# different ways to clear a list of elements

l1=[1,2,3,4,5,7,23,87]
print("initially list elements are ",l1)
print(l1.clear()) # by using clear()
del l1[:] # By using del keyword
print(l1)
# by using pop() func
print("By using pop()")
l2=[1,2,3,4,5,7,23,87]
while len(l2) != 0:
    l2.pop()
print(l2)
# by using reinialization
print("by using reinialization")
l3=[1,2,3,4,5,7,23,87]
l3=[]
print(l3)
l3=[1,2,3,4,5,7,23,87]
l3.clear()
print("by using clear() :",l3)

