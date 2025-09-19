"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Entradas
numero1 = input("Primer número: ")
numero2 = input("Segundo número: ")
numero3 = input("Tercer número: ")
primero = 0
segundo = 0
tercero = 0


# Proceso
if numero1 > numero2:
    segundo = numero1
    if numero1 > numero3:
        tercero = numero1
        if numero2 > numero3:
            primero = numero3
            segundo = numero2
        else:
            primero = numero2
            segundo = numero3
elif numero2 > numero3:
    tercero = numero2
    segundo = numero3
    if numero3 < numero1:
        primero = numero3
        segundo = numero1
else:
    primero = numero1
    segundo = numero2
    tercero = numero3



# Salidas
print("Números ordenados: " + str(primero) + " " + str(segundo) + " " + str(tercero))
