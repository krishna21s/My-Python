import random
choices = {1:"rock",2:"paper",3:"scissor"}
def uc(): 
    a = input("enter your choice: ")
    print(f"user's Choice is = {a}")
    return a
def aic():
    b= random.choice(choices)
    print(f"user's Choice is {b}")
    return b
if uc() == aic() :
    print("yes")
