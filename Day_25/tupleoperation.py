# Operations on Tuples in Python | Python Tutorial - Day #25

# https://www.youtube.com/watch?v=XblLSduioJI&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=25


# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp.append("Russia") # add item
# temp.pop(3) # remove item
# temp[2] = "Finland" # change item
# countries = tuple(temp)
# print(countries)


t=(1,2,3,4,5,1,2,3,4)
r=t.count(3)
print(r)

r=t.index(3)
print(r)

r=t.index(3,4,8)
print(r)

a=len(t)
print(a)

