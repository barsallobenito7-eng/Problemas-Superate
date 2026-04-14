stock = 67
precio_unitario = 15
ganancias_totales = 0

print("Bienvenidos")     
while stock > 0: 
    print(f"\nBienvenido. tenemos {stock} plugs")
    cantidad = int(input("Cuantos plugs quieres comprar?: "))

    if cantidad == 0:
       break


    if cantidad <= stock:
          subtotal = cantidad * precio_unitario


          if cantidad >=3:
             descuento =subtotal * 0.10
             total_venta = subtotal 
    