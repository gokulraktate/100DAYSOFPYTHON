class person:
    def __init__(self,n,o):
        print("Hey i am a person")

        self.name=n
        self.occ=o



    name="Gokul"
    occ="Developer"

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person("Gokul","Developer")
b=person("Sai","HR")

# a.name="Sai"
# a.occ="HR"
a.info()
b.info()