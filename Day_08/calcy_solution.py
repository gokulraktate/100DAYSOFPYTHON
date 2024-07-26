num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

choice = input("Choose an operator:\n 1) + \n 2) - \n 3) * \n 4) / \n 5)//\n 6)%\n: ")

if choice == '+':
    print("Addition: ", (num1 + num2))

elif choice == '-':
    print("Subtraction: ", (num1 - num2))    

elif choice == '*':
    print("Multiplication: ", (num1 * num2))    

elif choice == '/':
    print("Division ", (num1 / num2)) 

elif choice == '//':
    print("Flour Division ", (num1 // num2)) 

elif choice == '%':
    print("Mod is ", (num1 % num2)) 

else:
    print("Please enter valid operator")       
