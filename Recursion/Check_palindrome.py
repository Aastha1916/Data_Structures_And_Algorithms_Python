# METHHOD 1 : BY COMPARING WITH THE REVERSE OF GIVEN STRING

string = input()
n = len(string)
arr = list(string)
def reverse(arr,l):
    if l >= n//2:
        return 
    arr[l],arr[n-l-1] = arr[n-l-1],arr[l]
    reverse(arr,l+1)
reverse(arr,0)
if "".join(arr) == string:
    print("Yes !! It is a palindrome.")
else:
    print("No!! It is not a palindrome.")

#METHOD 2: BY USING TWO POINTERS COMPARISION OF EACH CHARACTER IN THE STRING (RECURSIVE)

string = input()
n = len(string)
def check(string,l,r):
    if l>=n//2:
        return True
    if string[l]!=string[r]:
        return False
    return True and check(string,l+1,r-1)


ans = check(string,0,n-1)
print(ans) 

#METHOD 3 : PARAMETERISED
string = input()
n = len(string)
def check(string,l,r):
    if l>=n//2:
        return True
    if string[l]!=string[r]:
        return False
    return check(string,l+1,r-1)


print(check(string,0,n-1))
