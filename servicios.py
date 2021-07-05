# Para crear el motor de base de datos con docker
#docker run --name mysql_productos -e MYSQL_ROOT_PASSWORD=123456 -d mysql:8.0
#Para instalar el conector de mysql:
#python3 -m pip install mysql-connector-python
#Base de datos con python:
#https://www.w3schools.com/python/python_mysql_getstarted.asp
from clases import Producto
import mysql.connector
class ProductosService:
 
    def conectar(self):
        self.con = mysql.connector.connect(host=self.servidor
        , user=self.usuario,password=self.clave, database=self.bd
        , auth_plugin="mysql_native_password")
    def desconectar(self):
        self.con.close()
    def __init__(self):
        self.servidor = "localhost"
        self.usuario = "root"
        self.clave = "123456"
        self.bd = "productos_db"
    def guardar(self,producto):
        self.conectar()
        cursor = self.con.cursor()
        sql = "INSERT INTO productos(nombre,valor,categoria,stock) VALUES(%s,%s,%s,%s)"
        valores = (producto.nombre,producto.valor,producto.categoria,producto.stock)
        cursor.execute(sql, valores)
        self.con.commit()
        self.desconectar()
    def obtenerTodos(self):
        self.conectar()
        cursor = self.con.cursor()
        cursor.execute("SELECT nombre,valor,categoria,stock FROM productos")
        resultado = cursor.fetchall()
        lista = []
        for r in resultado:
            producto = Producto(r[0],r[1],r[2],r[3])
            lista.append(producto)
        self.desconectar()
        return lista
