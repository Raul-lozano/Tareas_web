# Una escuela aplica dos exámenes a sus aspirantes, por lo 
# que cada uno de ellos obtiene dos calificaciones de notas
# como C1 y C2. El aspirante que obtenga una calificación mayor
# que 90 en cualquiera de los exámenes es aceptado; en caso contrario es rechazado.

class Escuela2:
    def init(self):
        pass
    def aspirantes (self):
        print("")
        C1=float(input("Escriba la primera nota"))
        C2=float(input("Escriba la segunda nota"))
        print("")
        if C1>=90 and C2>=90:
            print(("Sus Calificaciones son: {} , {} ").format(C1,C2))
            print("usted ha sido admitido")
        else:
            print(("Sus Calificaciones son: {} , {} ").format(C1,C2))
            print("usted ha sido rechasado")
        print("")
    aspirantes(" ")