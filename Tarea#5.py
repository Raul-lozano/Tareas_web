# Dado como dato la calificación de un alumno en un examen, 
# escriba “aprobado” si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.class Ejercicio5:
    def _init_(self):
        pass
    
    def Calificacion(self):
        print("")
        cal=float(input("Ingrese su calificacion:"))
        if cal >= 7 :
            print("Aprobado")
        else:
            print("Reprobado")
    Calificacion(" ")