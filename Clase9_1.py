productos= []

def agregar_producto():
    nombre = input("\nIngrese el nombre del producto que quiere agregar:").capitalize().strip()
    
     
    if nombre not in productos:
        
        precio = input("\nIngrese el precio del producto: ").strip()
        
        if precio.isdigit() and int(precio) >= 0:
            producto = {
                "nombre": nombre,
                "precio": precio
                }
            productos.append(producto)
            print("Producto agregado")
            print(f"\nNombre del producto: {nombre}  Precio: ${precio}")
            print()
            print()
            print("---Lista de productos actualizada---")
            for i, producto in enumerate(productos):
                print(f"{i+1}. Nombre del producto: {producto.get('nombre')}.  Precio: ${producto.get('precio')}\n")
            
    else:
        print(f"\nEl producto {nombre} está en la lista. No puede agregarse un producto existente.")
   
            
    
    
def mostrar_productos():
    
    if productos:
        print("Lista de productos")
        for i, producto in enumerate(productos):
            print(f"{i+1}. Nombre del producto: {producto.get('nombre')}.  Precio: ${producto.get('precio')}")
    else:
        print("La lista de productos está vacía.")
        print()
        
        
        
def borrar_producto():
                if productos:
                    borrar = input("Ingrese el nombre del producto que quiere borrar: ").capitalize()
                    for borrar in productos:
                        borrar.pop('nombre')
                        print(f"Producto'{borrar}' eliminado con éxito.\n")
                        print("---Lista de productos actualizada---")
                        for i, producto in enumerate(productos):
                            print(f"{i+1}. Nombre del producto: {producto.get('nombre')}.  Precio: ${producto.get('precio')}")
            
                    else:
                        print(f"El producto '{borrar}' no está en la lista.\n")
                else:
                    print("La lista de productos está vacía. No hay nada para borrar.\n")
                    
def mostrar_menu():                               
     while True:
         print("Menú de gestión de productos:")
         print("1. Agregar un producto")
         print("2. Consultar la lista de productos")
         print("3. Borrar un producto")
         print("4. Salir")
         
         opcion = input("Elige una opción del 1 al 4: ").strip()
         
         if opcion.isdigit:
             if 0 < int(opcion) <5:
                 
                 if int(opcion) == 1:
                   agregar_producto()
                 
                 elif int(opcion) == 2:
                   mostrar_productos()
                 
                 elif int(opcion) == 3:
                   borrar_producto()
                 
                 elif int(opcion) == 4:
                   print("Gracias por usar el programa. Chau.")
                   break
         else: 
             print("Opción no válida. Por favor, ingrese un número del 1 al 4 (incluidos).\n")
             
mostrar_menu()                  