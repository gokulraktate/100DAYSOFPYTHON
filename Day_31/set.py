# Sets in Python | Python Tutorial - Day #31

# https://www.youtube.com/watch?v=l3kCO8cVA6o&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=31

# SET is a collection of well defined objects.

#set is unordered collection
#no duplications allowed
s={2,3,4,5,3,2}
print(s)


#multi type elements allowed
info = {"Carla", 19, False, 5.9, 19}
print(info)


#this is empty dict
gokul={}
print(type(gokul))

#this is empty set
gokul=set()
print(type(gokul))

#for accessing
#no order maintained
for value in info:
    print(value)