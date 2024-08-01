# for Loop with else in Python | Python Tutorial - Day #35

# https://www.youtube.com/watch?v=qUkcIgErZzc&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=35


for i in range (5):
    print(i)
else:
    print("sorry no i")


for i in range (6):
    print(i)
    if i==4:
        break   #no further code will execute
else:
    print("sorry no i")


i=0
while i<7:
    print(i)
    i=i+1
else:
    print("sorry no i")
