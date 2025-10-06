class Producto:
    def __init__(self,nombre,precio,stook):
        self.nombre = nombre
        self.precio = precio
        self.stook = stook

    def __str__(self):
        return f"{self.nombre} -s/. {self.precio} stook: {self.stook}"

    def __eq__(self,otro):
        return self.nombre == otro.nombre

    def __add__(self,otro):
        return self.precio + otro.precio

    def __gr__(self,otro):
        return self.stook> otro.stook

prod1 = Producto("arroz",3.50,20)
prod2 = Producto("arroz",3.50,15)
prod3 = Producto("azucar",3.50,10)

print (prod1)
print (prod2)
print (prod3)

print(prod1==prod2)
print(prod1==prod3)

print(prod1 + prod2)
print(prod1 + prod3)

print(prod1 > prod3)
