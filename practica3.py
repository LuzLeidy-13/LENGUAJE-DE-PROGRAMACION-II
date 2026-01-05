from datetime import datetime

class Producto:
    
    def __init__(self, codigo, nombre, precio, stock=0):
        self.__codigo = codigo          # atributo encapsulado
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    # Getters
    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    # Métodos de negocio
    def agregar_stock(self, cantidad):
        if cantidad > 0:
            self.__stock += cantidad
        else:
            raise ValueError("La cantidad debe ser positiva")

    def retirar_stock(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.__stock:
            raise ValueError("Stock insuficiente")
        self.__stock -= cantidad

    def __str__(self):
        return f"{self.__codigo} | {self.__nombre} | Precio: S/. {self.__precio:.2f} | Stock: {self.__stock}"


class Movimiento:
    """Clase que registra entradas y salidas de productos"""

    def __init__(self, codigo_producto, tipo, cantidad):
        self.codigo_producto = codigo_producto
        self.tipo = tipo  # 'ENTRADA' o 'SALIDA'
        self.cantidad = cantidad
        self.fecha = datetime.now()

    def __str__(self):
        return f"{self.fecha.strftime('%d/%m/%Y %H:%M:%S')} - {self.tipo} - Producto: {self.codigo_producto} - Cantidad: {self.cantidad}"


class Inventario:
    """Clase principal que gestiona el inventario"""

    def __init__(self):
        self.__productos = {}   # diccionario encapsulado
        self.__movimientos = []

    # Registrar producto
    def registrar_producto(self, codigo, nombre, precio, stock_inicial=0):
        if codigo in self.__productos:
            raise ValueError("El producto ya existe")
        self.__productos[codigo] = Producto(codigo, nombre, precio, stock_inicial)

    # Entrada de stock
    def entrada_stock(self, codigo, cantidad):
        producto = self.__buscar_producto(codigo)
        producto.agregar_stock(cantidad)
        self.__movimientos.append(Movimiento(codigo, "ENTRADA", cantidad))

    # Salida de stock
    def salida_stock(self, codigo, cantidad):
        producto = self.__buscar_producto(codigo)
        producto.retirar_stock(cantidad)
        self.__movimientos.append(Movimiento(codigo, "SALIDA", cantidad))

    # Mostrar inventario
    def mostrar_inventario(self):
        print("\n--- INVENTARIO ACTUAL ---")
        if not self.__productos:
            print("No hay productos registrados")
        for producto in self.__productos.values():
            print(producto)

    # Reporte de movimientos
    def reporte_movimientos(self):
        print("\n--- REPORTE DE MOVIMIENTOS ---")
        if not self.__movimientos:
            print("No hay movimientos registrados")
        for mov in self.__movimientos:
            print(mov)

    # Reporte de productos con bajo stock
    def reporte_bajo_stock(self, limite=5):
        print(f"\n--- PRODUCTOS CON STOCK MENOR O IGUAL A {limite} ---")
        encontrados = False
        for producto in self.__productos.values():
            if producto.get_stock() <= limite:
                print(producto)
                encontrados = True
        if not encontrados:
            print("No hay productos con bajo stock")

    # Método privado
    def __buscar_producto(self, codigo):
        if codigo not in self.__productos:
            raise ValueError("Producto no encontrado")
        return self.__productos[codigo]

# Interfaz de consola


def menu():
    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Registrar producto")
    print("2. Entrada de stock")
    print("3. Salida de stock")
    print("4. Mostrar inventario")
    print("5. Reporte de movimientos")
    print("6. Reporte de bajo stock")
    print("7. Salir")


def main():
    inventario = Inventario()

    while True:
        try:
            menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                codigo = input("Código: ")
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                stock = int(input("Stock inicial: "))
                inventario.registrar_producto(codigo, nombre, precio, stock)
                print("Producto registrado correctamente")

            elif opcion == "2":
                codigo = input("Código del producto: ")
                cantidad = int(input("Cantidad de entrada: "))
                inventario.entrada_stock(codigo, cantidad)
                print("Entrada registrada")

            elif opcion == "3":
                codigo = input("Código del producto: ")
                cantidad = int(input("Cantidad de salida: "))
                inventario.salida_stock(codigo, cantidad)
                print("Salida registrada")

            elif opcion == "4":
                inventario.mostrar_inventario()

            elif opcion == "5":
                inventario.reporte_movimientos()

            elif opcion == "6":
                limite = int(input("Límite de stock: "))
                inventario.reporte_bajo_stock(limite)

            elif opcion == "7":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
