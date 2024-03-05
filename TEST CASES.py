import random
choices = {1:"rock",2:"paper",3:"scissor"}
def uc(): 
    a = input("enter your choice: ")
    print(f"user's Choice is = {a}")
    return a
def aic():
    b= random.choice(choices)
    print(f"AI's Choice is {b}")
    return b
k=uc()
l=aic()
def winner():
 o=["rock","paper","scissor"]
 if k==l:
    print(f"both are same")
 else:
    if k==o[0] and l==o[1]:
       print(f"User = {o[0]} \nAI = {o[1]}\n AI Won")
    if k==o[0] and l==o[2]:
      print(f"User = {o[0]} \nAI = {o[2]}\n User Won")
    if k==o[1] and l==o[0]:
      print(f"User = {o[1]} \nAI = {o[0]}\n User Won")
    if k==o[1] and l==o[2]:
      print(f"User = {o[1]} \nAI = {o[2]}\n AI Won")
    if k==o[2] and l==o[0]:
      print(f"User = {o[2]} \nAI = {o[0]}\n AI Won")
    if k==o[2] and l==o[1]:
      print(f"User = {o[1]} \nAI = {o[2]}\n AI Won")
winner()

