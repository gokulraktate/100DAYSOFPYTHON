# Match Case Statements in Python | Python Tutorial - Day #16

# https://www.youtube.com/watch?v=bthQCK1QAmQ

x = int(input("Enter the Number:"))

match x :
    
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _:                    #default case
        print("case is" ,x)  