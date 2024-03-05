'''l=[int(input("enter: ")),int(input("enter: ")),int(input("enter: ")),int(input("enter: ")),int(input("enter: "))]
max=l[0]
min=l[0]
for i in l:
    if i>max:
        max=i
    if i<min:
        min=i
print(f"maximum value = {max}")
print(F"minimum value = {min}")
approach: 1st consider max & min as '3'. use for loop & consider i, if i > max, then max becomes i.
Similarly, if i < min, then min becomes i. & final one print the max and min values.'''

#now easiest method:
l=[int(item) for item in input().split(",")]
l.sort()
print(f"the maximum = {l[-1]}, min = {l[0]}")
