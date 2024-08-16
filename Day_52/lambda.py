# def double(x):
#     return x*2


#use of lambda

def appl(fx,value):
    return 6 + fx(value)


double = lambda x:x*2
cube = lambda x:x*x*x
avg = lambda x,y,z:(x+y+z)/3

print(double(5))
print(cube(6))
print(avg(3,6,11))
print(appl(cube,2))
print(appl(lambda x:x*x*x,2)) #same as above

print(appl(lambda x:x*x,2)) #for square

