# String Methods in Python | Python Tutorial - Day #13

# youtube.com/watch?v=0INvoK_T0cE


#strings are immutable

a="!!! Gokul !!!!!!"
print(len(a))
print(a.upper())  #uppercase
print(a.lower())  #lowercase

#stripping
print(a.rstrip("!"))  #removes the all ! from tail

#replace
print(a.replace("Gokul","Sai")) #replace Gokul to Sai

#split
print(a.split(" ")) #splits  each element in list 

#capitalize
b="introduction to python"

print(b.capitalize()) #make first char to uppercase

#center()
c="This is center text"
print(c.center(50))

print(len(c))
print(len(c.center(50)))


#count()
d="python is easy,python is userfriendly"
print(d.count("python"))  #this counts how many time python word repeated

#endswith
b="Introduction to python!!!"
print(b.endswith("!!!"))   #if endswith !!! then it will show true otherwise false
print(b.endswith("...."))   
print(b.endswith("to",2,15))  #if ends with to at 14th index the show true

#find()
b="Introduction to python!!!"
print(b.find("to"))  #finds the index of to and write the index of first char if not the show error

#isalnum()

a="Hello123"
print(a.isalnum())  #if A-Z ,a-z and numbers(0-9) present then shows true

#isalpha()
s="Welcome"
print(s.isalpha())  #true because only alphabets present

s="Welcome12"
print(s.isalpha())   #false because numbers are present

#islower
a="gokul"
print(a.islower())   #if all lowercase then true

#isupper
a="GOKUL"
print(a.isupper())   #if all lowercase then true

#isprintable
a="this is printabble"
print(a.isprintable())  #if all the statement is printable then true

a="all this is printabble\n"  #\n is not printable
print(a.isprintable())


#isspace 
a="Hello"
b="     "
print(a.isspace())  #prints true if contains all empty space otherwise false
print(b.isspace()) 

title1 = "Gokul raktate"
print(title1.istitle())  #prints true if first letter of each word is capital

#startswith
s = "Python is a Interpreted Language"
print(s.startswith("Python"))


s = "Python is a Interpreted Language"
print(s.swapcase())   # upper to lower || vice-versa


s = "Python is a Interpreted Language"
print(s.title())