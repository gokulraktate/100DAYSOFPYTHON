# Set Methods in Python | Python Tutorial - Day #32

# https://www.youtube.com/watch?v=HOrutCnp2zo&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=32


s1={1,2,5,6}
s2={5,7,8}

#isdisjoint set
#print true if no common element
print(s1.isdisjoint(s2))


print(s1.union(s2))  #union method
print(s1,s2)
s1.update(s2)   #update method in which values of s2 will be added to s1 but common will be considered once
print(s1,s2)

s=s1.intersection(s2)
print(s)   #intersection method (only common values)

#symmetric diff
s=s1.symmetric_difference(s2)
print(s)     #values in s1 but common in s2 will be ignored

s=s1.symmetric_difference_update(s2)
print(s)     

#difference method
s=s1.difference(s2)
print(s)     #s1 - s2

#issuper set method
#true if yes otherwise false
s1={1,2,3,4,5}
s2={3,4}
print(s1.issuperset(s2))

#issub set method
#true if yes otherwise false
s1={1,2,3,4,5}
s2={3,4}
print(s2.issubset(s1))

#remove method
s1={1,2,3,4,5}
s1.remove(3)
print(s1)

#discard method
#same as remove but if element is not present it will not show error
s1.discard(66)
print(s1)

