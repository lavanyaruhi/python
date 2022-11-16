import timeit


#Reverse a String using join() and reversed()
mycode1='''
def reverse_join_reversed_iter(s):
    s1 = ''.join(reversed(s))
    return s1'''

#mysetup="from math import sqrt"

#Python Reverse String using List reverse()
mycode='''
def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)'''

print(timeit.timeit(setup='',
                    stmt=mycode,
                    number=1000000))

print("************************")
print(timeit.timeit(setup='',
                    stmt=mycode1,
                    number=10))
