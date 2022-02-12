import sys
argumentos = sys.argv

while True:
    try:
        año=int(argumentos[1])
        def año_bisiesto(año):
            if año%4 == 0 and año%100 != 0 or año%400 == 0:
                print("El año " +str(año)+ " es bisiesto")
            else:
                print ("El año "+str(año)+ " no es bisiesto")
            return año
        
        año_bisiesto(int(año))
        break
    except ValueError:
        print("Error: el parámetro no es un año")
        exit()