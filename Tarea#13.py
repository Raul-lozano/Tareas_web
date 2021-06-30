# Diseñe un pseudocódigo para calcular la suma y producto de 
# N números enteros, utilizando un bucle controlado por centinela.
 
class Calcular:
    def __init__(self):
         pass
    def centinela(self):
        print("")
        produc=1
        suma=0
        numero=int(input("Ingresar un numero entero"))
        print("")
        while numero != -1:
             numero=int(input("Ingresar un numero: "))
             suma=suma+numero
             prod=prod*numero
             print(" ")   
        print("""Total de la suma es:""",suma,"""Total del producto es: """,prod)
    centinela(" ")