# f-strings in Python | Python Tutorial - Day #28

# https://www.youtube.com/watch?v=ixmxgUf8yIg&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=28


# a="Hey my name is {} and i am from {}"
# name="Gokul"
# country="India"

# print(a.format(name,country))

# a="Hey my name is {1} and i am from {0}"
# name="Gokul"
# country="India"

# print(a.format(country,name))

name="Gokul"
country="India"

print(f"Hey my name is {name} and i am from {country}")

#for showing curly bracket as it is
print(f"Hey my name is {{name}} and i am from {{country}}")


b="The price is {price:.2f}"

print(b.format(price=145.6996740))



amount=1000.3242671
txt=f"The Total Amount is{amount:.2f}"
print(txt)


#print as a string
print(f"{2*20}")
print(type(f"{2*20}"))