saldo = 1000        # dinero que tiene el cliente en su cuenta
limite = 300        # límite máximo por retiro

while saldo > 0:
    print("Saldo disponible:", saldo)
    retiro = float(input("¿Cuánto dinero desea retirar? "))

    if retiro > limite:
        print("Error: excede el límite de retiro por operación.")
    elif retiro > saldo:
        print("Error: no tiene suficiente saldo.")
    else:
        saldo = saldo - retiro
        print("Retiro exitoso.")

    print()

print("Su cuenta quedó sin saldo.")
