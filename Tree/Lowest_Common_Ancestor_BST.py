# Method1
def lca1(root,p,q):
    if not root:
        return root
    if p.val==root.val or q.val==root.val:
        return root
    if p.val<root.val and q.val>root.val or q.val<root.val and p.val>root.val:
        return root
    elif p.val<root.val and q.val<root.val:
        return lca(root.left,p,q)
    elif p.val>root.val and q.val>root.val:
        return lca(root.right,p,q)

#Method2
def lca2(root):
    temp = root
    while temp:
        if p.val < temp.val and q.val < temp.val:
            temp = temp.left
        elif p.val > temp.val and q.val > temp.val:
            temp = temp.right
        else:
            return temp
            
root = [6,2,8,0,4,7,9,null,null,3,5]
p = 2
q = 8
ans1 = lca1(root,p,q)  # Method1
ans2 = lca2(root)   #Method2
        