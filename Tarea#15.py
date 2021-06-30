# Aplicar los pasos de la metodología para la solución de un 
# problema para leer un número entero N y calcular el resultado 
# de la siguiente serie

class Pasos:
    def __init__(self):
        pass
    def resultado(self):
        print("")
        i=1
        N= int(input("Ingresar un numero: "))
        print("")
        Num = 6
        serie=0
        for a in range(i,Num+1):
            Num=Num+6
            serie=serie+6
        print("La suma es:",serie)
        print("")
    resultado("")  