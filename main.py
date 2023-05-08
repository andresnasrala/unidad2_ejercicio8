from claseManejadorConjunto import ManejadorConjunto

def test(gestor):

    conjunto1 = input("Ingrese su conjunto separado por ; Para salir, ingrese FIN\n").upper()

    while conjunto1 != "FIN":
        conjunto2 = input("Ingrese el otro conjunto separado por ;\n")

        if gestor.crearConjuntos(conjunto1, conjunto2):
            gestor.operaciones()
            
        conjunto1 = input("Ingrese su conjunto separado por ; Para salir, ingrese FIN\n").upper()



if __name__ == '__main__':

    manejador = ManejadorConjunto()
    test(manejador)

    