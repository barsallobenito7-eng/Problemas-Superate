# Diccionario de usuarios (usuario: contraseña)
usuarios = {
    "admin": "1234",
    "juan": "abcd",
    "Benito": "2121"
}

# --- INICIO DE SESIÓN ---
intentos = 3
login_exitoso = False

while intentos > 0:
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print("Inicio de sesión exitoso\n")
        login_exitoso = True
        break
    else:
        intentos -= 1
        print("Datos incorrectos. Intentos restantes:", intentos)

if not login_exitoso:
    print("Acceso bloqueado")
else:
    
    
    # Diccionario de productos
    productos = {
        "pan": 0.50,
        "leche": 1.20,
        "huevos": 2.00,
        "arroz": 1.50
    }

    carrito = []

    while True:
        print("\n--- MENÚ ---")
        print("1. Ver productos")
        print("2. Comprar")
        print("3. Ver carrito")
        print("4. Pagar")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            # Bucle para mostrar productos
            for producto, precio in productos.items():
                print(producto, "-> $", precio)

        elif opcion == "2":
            nombre = input("Producto: ")
            
            if nombre in productos:
                cantidad = int(input("Cantidad: "))
                
              # (producto, cantidad)
                carrito.append((nombre, cantidad))
                print("Producto agregado")
            else:
                print("Producto no existe")

        elif opcion == "3":
            print("\n--- CARRITO ---")
            for item in carrito:
                print(item[0], "x", item[1])

        elif opcion == "4":
            total = 0
            
            # Bucle para calcular total
            for item in carrito:
                nombre = item[0]
                cantidad = item[1]
                precio = productos[nombre]
                
                subtotal = precio * cantidad  # operador aritmético
                total += subtotal
            
            impuesto = total * 0.07
            total_final = total + impuesto
            
            print("Total:", total)
            print("Impuesto:", impuesto)
            print("Total a pagar:", total_final)

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")