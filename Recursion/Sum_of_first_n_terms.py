# METHOD 1: Recursive

n = int(input())

def sum(n):
    if n==0:
        return 0
    return n + sum(n-1)

s1 = sum(n)
print(s1)

#METHOD 2: Parameterised

n = int(input())
def sum(n,s1):
    if n==0:
        print(s1)
        return 
    sum(n-1,s1+n)

sum(n,0)

