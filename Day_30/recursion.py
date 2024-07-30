# Recursion in Python | Python Tutorial - Day #30

# https://www.youtube.com/watch?v=XYwJKFB8DUk&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=30



#factorial (0)=1
#factorial (5)=5*4*3*2*1

#factorial(n)=n*factorial(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))
print(factorial(7))

#4 * factorial(3)
#4 * 3 * factorial(2)
#4 * 3 * 2 * factorial(1)


#fibonacci sequence

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))  