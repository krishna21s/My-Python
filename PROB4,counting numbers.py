'''l=[1,2,3,2,1,4,2,5]
k=int(input("enter: '))
m=0
for i in l:
  if i==k:  
    m+=1
print(f"count of {k} = {m}")
'''
#or
#1,2,3,2,1,4,2,5
'''l=[int(item) for item in input().split(",")]
n=int(input("enter the n value: "))
count=0
for i in l:
    if i==n:
        count+=1
print(count)'''
#easiest method:
l=[int(item) for item in input().split(",")]
n=int(input("enter n value: "))
k=l.count(n)
print(k)
