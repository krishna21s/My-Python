a=float(input('enter a: '))
b=float(input("enter b: "))
c=float(input("enter c: "))
root1=(-b+((((b**2)-(4*a*c))**0.5)))/2*a
root2=(-b-((((b**2)-(4*a*c))**0.5)))/2*a
def roots(a,b,c):
    return f"the roots are {root1,root2}"
value=roots(a,b,c)
print(value)