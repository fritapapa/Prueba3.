import csv
inventario = [] 
def menu():
    
    op = "0"
    while op != "4":
        print ("*** Inventario: ***")
        print("[1].... Agregar al inventario:")
        print("[2].... Leer inventario:")
        print("[3].... Clasificar y exportar:")
        print("[4].... Salir")
        op = input("Seleccione una opción del 1 al 4:")

        if op == "1":
            agregar_productos_inventario()
        elif op == "2":
            leer_inventario()
        elif op == "3":
            clasificar_exportar
        elif op == "4":
            print ("adios")
        else:
            print ("error")

def agregar_productos_inventario():
    agregar = input("ingrese producto deseado:")
    ID = int(input("ingresa id del producto:"))
    categoria = input("ingresa categoria del objeto (electronica, textil o calzado):")
    precio = float(input("ingresa valor del producto"))
    with open ('inventario.csv', 'a', newline='') as archivo_inventario:
        for nombre in inventario:
            escribir = csv.writer(archivo_inventario)
            escribir.writerow([nombre, ID, categoria, precio])

def leer_inventario():
    print("* Inventario de productos *")
    try:
        with open('inventario.csv', 'r', newline='') as archivo_csv:
            reader = csv.reader(archivo_csv)
            for producto in reader:
                print(producto)
    except FileNotFoundError:
        print("El inventario está vacío. Aún no se han agregado productos.")


def clasificar_productos():
    print("*** Clasificación de productos y generación de archivo de texto ***")
    categorias = {
        'Electrónica': [],
        'Textil': [],
        'Calzado': []
    }

    try:
        with open('inventario.csv', 'r', newline='') as archivo_csv:
            reader = csv.reader(archivo_csv)
            next(reader)  
            for producto in reader:
                categoria = producto[2]
                if categoria in categorias:
                    categorias[categoria].append(producto)

        if any(categorias.values()):
            with open('clasificacion_productos.txt', 'w') as archivo_txt:
                for categoria, productos in categorias.items():
                    if productos:
                        archivo_txt.write(f"{categoria}:\n")
                        for producto in productos:
                            archivo_txt.write(f"{', '.join(producto)}\n")
            print("Archivo generado correctamente.")
        else:
            print("No hay productos en el inventario para clasificar.")
    except FileNotFoundError:
        print("El inventario está vacío. Aún no se han agregado productos.")