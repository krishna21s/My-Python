'''l=[10,20,30,20,40,10,50]
n=[]
for i in l:
    if i in n:
        continue
    else:
        n.append(i)
print(n)'''
#or easier method:
'''l=[10,20,30,20,40,10,50]
k=set(l)
n=list(k)
n.sort()
print(n)'''
#or
l=[int(item) for item in input().split(",")]
k=set(l)
n=list(k)
n.sort()
print(n)