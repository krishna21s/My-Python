a,b=map(int,input("enter a,b values: ").split(","))
d1=[]
d2=[]
f=[]
for i in range(1,a+1):
    if a%i==0:
        d1.append(i)
for i in range(1,b+1):
    if b%i==0:
        d2.append(i)
d1=set(d1)
d2=set(d2)
s=d1.intersection(d2)
if s:    
  f=max(s)
  print(f"the GCD = {f}")
else:
   print("there is no gcd")