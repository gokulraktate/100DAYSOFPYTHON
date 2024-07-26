# Function Arguments in Python | Python Tutorial - Day #21

# https://www.youtube.com/watch?v=0d6b6fFuCkE


# def average(a,b):
#     print("average is:",(a+b)/2)

# average(2,3)


#default argument
def average(a=3,b=6):
    print("average is:",(a+b)/2)

average()
average(2)   #here a=2
average(b=4)
average(b=20,a=5)



# REQUIRED ARGUMNETS

def average(a, b = 5, c = 7):
    print("The average is", (a+b+c) / 3)
    
average(9)    


def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is:",sum/len(numbers))

average(7,8)





# def name (**name):
#     print(type(name))
    
#     print("Hello", name["fname"], name["mname"], name["lname"])

# name(fname = "Gokul", mname = "Sanjay", lname = "Raktate")