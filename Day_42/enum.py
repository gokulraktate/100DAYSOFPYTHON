# Enumerate Function in Python | Python Tutorial - Day #42

# https://www.youtube.com/watch?v=kGnYc_h1geM&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=42

# enumerate => inbuilt function

# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.

# The enumerate() function adds a counter as the key of the enumerate object.

marks=[33,44,55,66,88,99,1,4,6]

# index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("Awesome")
#     index +=1



for index, mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("Awesome")
 

a=[11,22,33,44,55,66]
for index,value in enumerate(a):
    print(index,value)

a=["one","two","three"]
for index,value in enumerate(a):
    print(index+1,":",value)

