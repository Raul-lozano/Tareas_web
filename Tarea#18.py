#Se tiene información sobre las calificaciones de 6 exámenes de un grupo de 30 alumnos. Los datos sobre estos exámenes se proporcionan de la siguiente manera:

class Ejercicio18:
    def _init_(self):
        pass
    def Calificaciones(self):
        print("")
        i=0
        j=0
        for i= 1 in 30:
            for j == 1 in 6:
            print ("Escriba la calificación del alumno",i, "en el examen",j)
            i,j=input ("ingrese las calificaciones de estudiantes") 
        for j == 1 in 6:
            sum = 0
            for  i = 1 in 30 :
            sum = sum + i,j
            prom = sum/30
            print("promedio examen",j , prom)
            for i = 1 in 30:
            sum = 0
            for j==1 in 6:
            sum = sum + i,j
            print("promedio del alumno",i,sum/6)
        Examen = 1
        promayor = prom[1]
        for  j==2  in 6:
            if promayor < prom :
                promayor = prom
                Examen = j
            print ("el examen", Examen, "obtuvo el mayor promedio= ", promayor)
            print("")
            print("")
            
Calificacion(" ")