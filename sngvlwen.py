

Total_de_estudiantes = int (input("ingrese el total de alumnos inscritos en el colegio"))
Asistieron_hoy = int (input("Cuantos alumnos cruzaron las puerta hoy?"))

Faltaron = Total_de_estudiantes - Asistieron_hoy

Porcentaje_asistencia  = (Asistieron_hoy / Total_de_estudiantes) *100

es_buen_dia = Porcentaje_asistencia > 90

print("\n Reporte general")

print(f"Total de los niños:{Total_de_estudiantes} alumnos")
print(f"faltaron a clase: {Faltaron} estudiantes")
print(f"asistencia:n{Porcentaje_asistencia}%")


if es_buen_dia and (Faltaron ==0):
    print("omg si beba")
elif es_buen_dia:
    print("nyamete") 
else: 
    print ("i am super happy wao")