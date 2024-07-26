# If Else Conditional Statements in Python | Python Tutorial - Day #14

# https://www.youtube.com/watch?v=ceiuLR2ysas

# conditional operators
# > < >= <= == !=

a= int(input("Enter your age: "))
print("Your age is", a)

if(a>= 18):
    print("you can drive")

else:
    print("you can not drive")

print("this is outside the loop")

print(a<18)
print(a<=18)
print(a==18)
print(a!=18)


#if-elif-else

num=int(input("enter the no:"))
if(num<0):
    print("no is negative")

elif (num==0):
    print("no is Zero")

else:
    print("no is positive")

print("Thank You")


#nested if-else

num=18
if (num<0):
    print("negative")

elif(num>0):
    if(num<=10):
        print("num is between 1-10")
    else:
        print("num is greater than 10")
else:
    print("num is zero")