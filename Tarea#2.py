# En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente desea 
# saber cuánto deberá pagar finalmente por su compra.

class Ejercicio2:
    def _init_(self):
        pass
    
    def ejecutar():
        TC = float(input("Ingrese total de la compra:"))
        D = TC*0.15
        CP = TC - D
        print("Su cantidad a pagar es:")
        print (CP,"$")
    ejecutar()