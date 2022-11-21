# add list to tuble and vs



t1=(3,7,6,9)
l1=[7,6,9,8]
#t1=list(t1) # tuple converts to list then add
print(list(t1)+l1)  # list
print(tuple(l1+list(t1)))  # tuple
