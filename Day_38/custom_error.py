# Raising custom errors in Python | Python Tutorial - Day #38

# https://www.youtube.com/watch?v=Phr4CNppYoM&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=38


a=int(input("enter any value between 5 and 9 : "))

if(a<5 or a>9):

    raise ValueError("Value should be between 5 and 9") 
    #custom error


a=input("enter any value between 5 and 9 : ")

if(a=="quit"):
    print("OK")

elif(int(a)<5 or int(a)>9):

    raise ValueError("Value should be between 5 and 9") 
    #custom error

