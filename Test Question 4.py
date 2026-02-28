class Product:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def display(self):
        print(f'{self.id} - {self.name}')

class A(Product):
    def __init__(self, id, name,count = 50,category = "butter"):
        super().__init__(id, name)
        self.count = count
        self.category = category
    
    def display(self):
        super().display()
        print(f'{self.count} - {self.category}')

class B(Product):
    def __init__(self, id, name,count = 90,category = "Milk"):
        super().__init__(id, name)
        self.count = count
        self.category = category
    
    def display(self):
        super().display()
        print(f'{self.count} - {self.category}')

class C(Product):
    def __init__(self, id, name,count = 56,category = "choco"):
        super().__init__(id, name)
        self.count = count
        self.category = category
    
    def display(self):
        super().display()
        print(f'{self.count} - {self.category}')


A1 = A(15927,'Amul')
A1.display()

B1 = B(18927,"Heritage")
B1.display()

C1 =C(192083,"Kellongs")
C1.display()