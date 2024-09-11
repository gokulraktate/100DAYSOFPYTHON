#class and object



class Person:
    name="Gokul"
    occupation="Software Developer"
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person()
b=Person()

a.name="Raktate"
a.occupation="Tester"

b.name="Sai"
b.occupation="Farmer"
# print(a.name,a.occupation)

a.info()
b.info()