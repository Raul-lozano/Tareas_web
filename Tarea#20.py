# Una escuela aplica dos exámenes a sus aspirantes, por lo que 
# cada uno de ellos obtiene dos calificaciones de notas como 
# C1 y C2. El aspirante que obtenga calificaciones mayores que 
# 80 en ambos exámenes es aceptado; en caso contrario es rechazado.

class Escuela:
    def init(self):
        pass
    def notas (self):
        print("")
        C1=float(input("Escriba la primera nota"))
        C2=float(input("Escriba la segunda nota"))
        if C1>=80 and C2>= 80:
            print(("Sus Calificaciones son: {} , {} ").format(C1,C2))
            print("usted ha sido admitido")
        else:
            print(("Sus Calificaciones son: {} , {} ").format(C1,C2))
            print("usted ha sido rechasado")
        print("")
    notas(" ")