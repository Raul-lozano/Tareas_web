#Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.

class Ejercicio8:
    def _init_ (self):
        pass
    def Numero (self):
        n1= int(input("Ingresar primer numero:"))
        n2= int(input("Ingresar segundo numero:"))
        n3= int(input("Ingresar tercer numero:"))
        print(" ")
        if n1>n2 and n1> n3:
            nM =n1
        else:
            if n2>n3:
                nM= n2
            else:
                nM= n3
        print("El numero Mayor es:",nM)
        print(" ")
    Numero(" ")