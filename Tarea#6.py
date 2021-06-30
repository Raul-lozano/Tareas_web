#Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento.

class Ejercicio6:
    def _init_(self):
        pass
    def Empleado (self):
        print(" ")
        sue= float(input("sueldo del empleado:"))
        if sue < 600: 
            NS = sue+sue*0.1
            print()
        else:
            NS = sue 
            print()
        print("Nuevo sueldo:")
        print(NS)
    Empleado(" ")