def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1) 


print("rec:",fact(3))
print("rec:",fact(5))