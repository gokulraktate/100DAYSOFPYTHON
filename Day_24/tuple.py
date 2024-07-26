# Tuples in Python | Python Tutorial - Day #24

# https://www.youtube.com/watch?v=PipsOUDKrVk&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=24

# Tuple can not change i.e immutable


t=(1,4,5,6,"abc")
print(type(t))
print(t)

# t[0]=10
# print(t)  cants print because it is immutable
print(len(t))

print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])


if 5 in t:
    print("yes")
else:
    print("no")

t2=t[1:4]
print(t2)

