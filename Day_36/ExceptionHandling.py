# Exception Handling in Python | Python Tutorial - Day #36

# https://www.youtube.com/watch?v=4LKo6dlku7M&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=36

a=input("enter a number:")
print(f"Multiplication table of {a} is:")


#exception handling
try:
     for i in range(1,11):
         print(f"{a} X {i}={int(a)*i}")
except Exception as e:
     print(e)

print("End of Program")

#or

try:
     for i in range(1,11):
         print(f"{a} X {i}={int(a)*i}")
except :
     print("Some error occurs")

print("End of Program")


#multiple exception handling
try:
     num=int(input("enter the integer:"))
     a=[2,4]
     print(a[num])
except ValueError:
     print("number entered is not a integer")

except IndexError:
     print("Index error")