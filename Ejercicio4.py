cesta = {}

print("Introduce los productos de la compra (escribe 'fin' para terminar)")

while True:
    producto = input("Producto: ")
    
    if producto.lower() == "fin":
        break
    
    precio = float(input("Precio: "))
    cesta[producto] = precio

print("\nLista de la compra:")

total = 0

for producto, precio in cesta.items():
    print(f"{producto} | {precio}")
    total += precio

print(f"Total: {total}")