import sys
argumentos = sys.argv
if len(argumentos) !=3:
    print("Error: cantidad de argumentos incorrecta")
    sys.exit(1)
n1, n2= argumentos[1],argumentos[2]

def suma_dos_numeros(numero1: int,numero2: int) -> int:
    # Acciones a realizar
    if type(numero1)==int and type(numero2)==int:
        resultado = numero1 + numero2
    else:
        raise("Error: los argumentos no son números")
    return resultado

resultado_suma = suma_dos_numeros(int(n1),int(n2))
print(resultado_suma)