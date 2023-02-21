#Recursion
def f(n1):
    if n1<=1:
        return n1
    return f(n1-1)+f(n1-2)

n = int(input())
ans = f(n)
print(ans)

#Memoization
a=[-1]*6
a[0]=0
a[1]=0
a[2]=1
def fib(n):
    if a[n]!=-1:
        return a[n]
    else:
        a[n]=fib(n-1)+fib(n-2)
fib(5)
print(a[5])
