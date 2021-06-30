#ejercicio12
#Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por el usuario.

class Ejercicio12:
    def _init_(self):
        pass
    def Suma (self):
        suma =0
        prod =0
        resp = input(str("Ingresar numeros (S / N)" ))
        while  resp!= "N" and resp!= "n":
            num = int ( input ( "Ingrese un numero:" ))
            print(" ")
            suma = suma+num
            prod = prod*num
            resp = input ( "Desea continuar (S / N)?:")
        print ( "Total de la suma es:", suma)
        print ("Total del producto es:" , prod )
        print("")
    Suma(" ")