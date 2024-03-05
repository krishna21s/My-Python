add,sub,mul,div=0,0,1,1
des=input("select the operation[+,-,*,/]: ")
if des=="+":
  x=[int(item) for item in input().split("+")]
  add=sum(x)
  print(f"sum = {add}")
elif des=="-":
  x=[int(item) for item in input().split("-")]
  sub=x[0]-sum(x[1:])
  print(f"subtract = {sub}")
elif des=="*":
  x=[int(item) for item in input().split("*")]
  for i in x: 
     mul*=i
  print(f"multiply = {mul}")
elif des=="/":
  x=[int(item) for item in input().split("/")]
  if len(x) >1 and 0 not in x[1:]:
   div=x[0]
   for i in x[1:]:
    div/=i 
    print(f"divide = {div}")
  else: 
    print("ERROR: Division by zero or incorrect input")
else:
    print("Invalid operation selected")
