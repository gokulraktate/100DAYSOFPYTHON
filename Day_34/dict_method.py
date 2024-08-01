# Dictionary Methods in Python | Python Tutorial - Day #34

# https://www.youtube.com/watch?v=LmbFwaLjT9k&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=34


ep1={122:45,89:90,444:69}
ep2={222:70,555:80,888:90}

#update method
ep1.update(ep2)
print(ep1)

#clear method
# ep1.clear()
# print(ep1)


#to delete last key value pair
ep1.popitem()
print(ep1)

#to delete the total ep1
# del ep1
# print(ep1)

#to delete specific data entry/key value pair
del ep1[122]
print(ep1)