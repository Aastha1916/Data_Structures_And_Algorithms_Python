def find_subsequences(idx,temp,subsequences):
    if idx >= n:
        subsequences.append("".join(temp))
        return
    temp.append(string[idx])
    find_subsequences(idx+1,temp,subsequences)
    temp.pop()
    find_subsequences(idx+1,temp,subsequences)

string = input()
n = len(string)
temp = []
subsequences = []
find_subsequences(0,temp,subsequences)
print(subsequences)
