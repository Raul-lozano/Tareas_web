#Calcular el factorial de N números enteros leídos de teclado.El problema consistirá en realizar una estructura de N iteraciones aplicando el factorial de un número.

class Ejercicio16 :
    def _init_(self):
        pass
    def  Factorial(self):
        print("")
        l = 1
        n = int (input("ingrese un numero para la serie:"))
        print("")
        s = 5
        ser = 0
        for a in range ( l , n + 1 ):
            s = s + 5
            ser = ser + s
        print ( "la suma de la serie es:" , ser )

        print("")
    Factorial("")