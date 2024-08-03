# Finally keyword in Python | Python Tutorial - Day #37

# https://www.youtube.com/watch?v=r_iuC-IDpPM&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=37



def func1():

     try:
         l=[1,2,3,4]
         i=int(input("enter the index:"))
         print(l[i])
         return 1
     except:
         print("some error occurred")
         return 0
     
     finally:
         print("I am always executed")
    #  print("I am always executed")
x=func1()
print(x)