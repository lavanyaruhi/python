# wap to find given number is fibnocci or not
N=int(input("enter integer : "))
f3=0
f2=1
f1=1
if (N==0 or N==1):
    print("N is fibb")
else:
    while f3<N:
        f3=f1+f2
        f2=f1
        f1=f3
    if f3 == N:
        print(f"{N} is fibbnoc")
    else:
        print(f"{N} is not fobbnoic")
