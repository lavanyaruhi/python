import timeit


#Reverse a String using While Loop
def reverse_while_loop(s):
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1
input_str = 'ABç∂EF'
mycode= '''if __name__ == "__main__":
    print('Reverse String using while loop =', reverse_while_loop(input_str))
'''
print(timeit.timeit(setup='',
                    stmt=mycode,
                    number=10000000))

#Reverse a String using join() and reversed()
def reverse_join_reversed_iter(s):
    s1 = ''.join(reversed(s))
    return s1
str="sana"
print(reverse_join_reversed_iter(str))


#Python Reverse String using List reverse()
def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)

print(reverse_list('neha'))
