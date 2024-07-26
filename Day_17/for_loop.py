# For Loops in Python | Python Tutorial - Day #17

# https://www.youtube.com/watch?v=fIYVzKp0q5w


name="Gokul"
for i in name:
    print(i)

name="Gokul"
for i in name:
    print(i,end=",")

#list
print("\n")
colors=["red","yellow","blue","green"]
for color in colors:
    print(color)
    
    for i in color:
        print(i)

#range

for i in range(0,201):  #num from 0 to 200
    print(i)

for i in range(100,201):  #num from 100 to 200
    print(i)

for i in range(20):  #num from 0 to 200
    print(i)


for k in range(1,12,3):    #1 to 12 but only the number having gap of 3 i.e 1, 4(1+3),7(4+3).....
    print(k)