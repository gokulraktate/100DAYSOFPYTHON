# Introduction to Lists in Python | Python Tutorial - Day #22

# https://www.youtube.com/watch?v=eF6nK5bSlmg&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=22


# l=[3,4,5]
# print(l)
# print(type(l))


marks=[30,40,50,"Gokul",5.6,True]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4]) 

# print(marks[-3])  #negative index
# print(marks[len(marks)-3])  #positive index


# if 7 in marks:
#     print("yes")
# else:
#     print("No")


# #same for string
# if "kul" in "Gokul":
#     print("Yes")
# else:
#     print("No")

print(marks)

print(marks[1:-2])

print(marks[1:5:2])  #jumpindex


list=[i for i in range(4)]
print(list)

list=[i*i for i in range(4) if i%2==0]  
print(list)