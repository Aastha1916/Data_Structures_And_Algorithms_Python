#Recursion
def f(n1):
    if n1==1:
        return 0
    if n1 ==2:
        return 1 
    return f(n1-1)+f(n1-2)

n = int(input())
ans = f(n)
print(ans)

#Memoization
def fib(n):
    if n == 1:
        a[n] = 0
        return a[n]
    if n == 2:
        a[n] = 1
        return a[n]
    if a[n]!=-1:
        return a[n]
    a[n]=fib(n-1)+fib(n-2)
    return a[n]

n = int(input())
a=[-1]*(n+1)
print(fib(n))
print(a)


#iterative
n = int(input())
a = 0
b = 1
if n == 1:
    print(0)
if n == 2:
    print(1)
if n > 2:
    for _ in range(3,n+1):
        a,b = b,b+a
    print(b)

