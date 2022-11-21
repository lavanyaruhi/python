# WAP to find largest element in array
def largest_ele_array(arr,n):
    max = arr[0]
    for i in range(1,n):
        if arr[i] > max:
            max=arr[i]

    return max
arr=[10,40,65,76,43]
n=len(arr)
# By using max() to get largest element in array
Lele=max(arr)
print("large number in array:%s"%Lele)
# by using sort to get largest element in array
ele=sorted(arr)
print(ele)
print(ele[n-1])
#by using function
print(largest_ele_array(arr,n))
# by using sort()
arr.sort()
print(arr[n-1])
