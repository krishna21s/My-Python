t=float(input("enter C(1)\F(2)\K(3): "))
ctof=(t*9/5)+32
ctok= t+273
ftoc=(t-32)*5/9
ftok=((t-32)*5/9)+273
ktoc=t-273
ktof=((t-273)*9/5)+32

if t==1:
    def temp(a,b,c):
      a=float(input("enter celcius: "))
      b=ctof
      c=ctok
      final=temp(a,b,c)
      print(final)
    
   

    