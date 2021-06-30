#ejercicio14 
#Determinar si un número entero proporcionado por el usuario es primo. Un número primo es un entero que no tiene más divisores que él mismo y la unidad. Elaborar Pseudocódig

class Ejercicio14:
    def init(self):
        pass
    def Numero(self):
        primo=0
        divisor= 2
        num=int(input("Ingrese un numero entero:"))
        print("")
        
        while divisor < num and primo ==0:
            Res= divisor < num
            print(Res)
            if Res ==0:
                primo += 1
            divisor +=1
        if primo == 0:
            print("Numero",num,"es primo ") 
        else:
            print("Numero",num,"no es primo")
            print()
        print("")
    Numero("")