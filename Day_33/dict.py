# Dictionaries in Python | Python Tutorial - Day #33

# https://www.youtube.com/watch?v=j2G68uQtOwM&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=33


#dictionary is combination of 'key value' pair

d={
    "a":"Gokul",
    "b":"Raktate",
    1:"Roll"
}

print(d)
print(d["a"])  #key is entered and value is printed

#print all keys
print(d.keys())

#print all values
print(d.values())

#print key value pair
print(d.items())

#accessing values by iteration 
for key in d.keys():
    print(d[key])

