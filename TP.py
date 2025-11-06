archivo = open("productos.txt", "a")
archivo.close()

productos = []
archivo = open("productos.txt", "r")
lineas = archivo.readlines()
archivo.close()

for linea in lineas:
    linea = linea.strip()
    if linea:  # Ignorar lineas vacias
        datos = linea.split(",")
        producto = {
            "nombre": datos[0],
            "precio": float(datos[1]),
            "cantidad": int(datos[2])
        }
        productos.append(producto)


while True:
    print("""
    Menu de productos
    1) Ver productos
    2) Agregar producto
    3) Buscar producto
    4) Salir
    """)

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        if not productos:
            print("No hay productos cargados.")
        else:
            print("Lista de productos:")
            for prod in productos:
                print(f"Producto: {prod['nombre']} | Precio: ${prod['precio']} | Cantidad: {prod['cantidad']}")

    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
        nuevo_producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        productos.append(nuevo_producto)
        
        archivo = open("productos.txt", "a")
        archivo.write(f"{nombre},{precio},{cantidad}\n")
        archivo.close()
        print(f"Producto {nombre} agregado correctamente.")

    elif opcion == "3":
        buscar = input("Ingrese el nombre del producto a buscar: ")
        encontrado = False
        for prod in productos:
            if prod["nombre"].lower() == buscar.lower():
                print(f"Producto encontrado: {prod['nombre']} | Precio: ${prod['precio']} | Cantidad: {prod['cantidad']}")
                encontrado = True
                break
        if not encontrado:
            print("El producto no existe en la lista.")

    elif opcion == "4":
        print("Gracias por utilizar el programa.")
        break

    else:
        print("Opcion incorrecta, intente de nuevo.")
