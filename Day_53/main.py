def cube(x):
    return x*x*x

print(cube(3))


l=[1,2,4,5,7,8]
# newl=[]
# for i in l:
#     newl.append(cube(i))

# print(newl)

#map
newl=list(map(cube,l))   #use of map
print(newl)


#filter
def filter_fun(a):
    return a>4
newl1=list(filter(filter_fun,l))  #use of filter
print(newl1)


# reduce

from functools import reduce
no=[1,2,3,4,5]

sum=reduce(lambda x,y:x+y,no)  #use of reduce

print(sum)