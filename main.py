from clases import Producto
from servicios import ProductosService
"""
    Administrador de productos:
    Ingresar productos en bd
    Listarlos
"""
productoService = ProductosService()
def agregarProducto():
    global productoService
    nombre = ""
    while nombre == "":
        nombre = input("Ingrese nombre:").strip()
        if nombre == "": print("El nombre no puede ser vacio!")
    valor = -1
    while valor <= 0:
        try:
            valor = int(input("Ingrese valor del producto:"))
            if valor <=0: print("El valor no puede ser negativo")
        except:
            print("Oie hermano,el valor debe ser positivo y numero")
    stock = -1
    while stock <0:
        try:
            stock = int(input("Ingrese stock actual:"))
            if stock <0: print("No existe el stock negativo")
        except:
            print("El stock debe ser numerico")
    categoria = ""
    while categoria == "":
        categoria = input("Ingrese categoria:").strip()
        if categoria == "": print("Oie hermano, ingresa categoria")
    #Crear un producto!!!
    producto = Producto(nombre,valor,categoria,stock)

    productoService.guardar(producto)


def mostrarProductos():
    global productoService
    productos = productoService.obtenerTodos()
    for p in productos:
        print(p)


def menu():
    continuar = True
    print("Bienvenido:")
    print("1. Ingrese Producto")
    print("2. Mostrar Productos")
    print("0. Salir")

    opcion = input()
    if opcion == "1": agregarProducto()
    elif opcion == "2": mostrarProductos()
    elif opcion == "0": continuar = False
    else: print("Aprete bien, care logi")

    return continuar

while menu(): pass

