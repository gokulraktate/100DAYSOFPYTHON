import random
def check(a,b):
    if a==b:
        return 0
    elif(a==0 and b==1):
        return -1
    elif(a==1 and b==2):
        return -1
    elif(a==2 and b==0):
        return -1
    else:
        return 1


a=random.randint(0,2)
b=int(input("0 for snake, 1 for water and 2 for gun:"))

score=check(a,b)
print("You:",a)
print("Comp:",b)

if(score==0):
    print("Draw")
elif score==1:
    print("Lose")
else:
    print("Won")