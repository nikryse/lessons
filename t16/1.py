class Cat:
    def  __init__(self,name, color, age):
        self.name = name
        self.color = color
        self.age = age
    def myau(self):
        print(self.name + " says myau!")
    def murmur(self):
        print(self.name + " mur-mur")
    def gavgav(self):
        print(self.name + " gav-gav")
cat_1 = Cat(name= "Leon lox", color = "blue", age = "12")
print(cat_1.color)
print(cat_1.age)
print(cat_1.name)
cat_1.myau()
cat_1.murmur()
cat_1.gavgav()
