#Definir el molde
class Producto:

    #Constructor, funcion que se ejecuta cuando el producto nace
    def __init__(self, nombre,valor,categoria,stock):
        #La clase tiene atributos/caracteristicas
        self.nombre = nombre
        self.valor = valor
        self.categoria = categoria
        self.stock = stock
    def getIVA(self):
        return int(self.valor * 0.19)
    def getTotal(self):
        return self.valor + self.getIVA()
    #Forma de presentarse del objeto en el mundo
    def __str__(self):
        return f"nombre:{self.nombre} cat:{self.categoria} valor:{self.valor} stock:{self.stock} total:{self.getTotal()}"

class Pokemon:

    def __init__(self, nombre,tipo,sexo):
        self.nombre = nombre
        self.tipo = tipo
        self.sexo = sexo

