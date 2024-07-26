# Strings in Python | Python Tutorial - Day #11

# https://www.youtube.com/watch?v=kMNFQYArrLg

#string
name="Gokul"
friend="Prasad"
anotherFriend="Krishna"

print("Hello,"+name)

print(name[0])  #element at 0th position
print(name[1])  #element at 1th position
print(name[2])  #element at 2th position
print(name[3])  #element at 3th position
print(name[4])  #element at 4th position

#multi line string
a='''
hi 
hello
i am Gokul'''

print(a)

print("lets use a for loop\n")

#to print all character we use for loop
for character in name:
    print(character)


for character in a:
    print(character)