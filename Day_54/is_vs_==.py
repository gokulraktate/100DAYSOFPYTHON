a=4
b="4"

print(a is b)   #exact location of object in memory
print(a == b)   #value

a=4
b=4
print(a is b) #true
# print(a == b) #true

a=[1,2,3]
b=[1,2,3]

print(a is b) #exact location of object in memory  #false
print(a == b) #true


a="ok"
b="ok"

print(a is b) #exact location of object in memory  #false
print(a == b) #true



a=(1,2)    
b=(1,2)
#tuple is immutable so a and b both values stored in same memory location
print(a is b) #exact location of object in memory  #false
print(a == b) #true


a=None
b=None
print(a is b)
print(a is None)
