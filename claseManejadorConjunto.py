from claseConjunto import Conjunto

class ManejadorConjunto:


    def __init__(self):
        self.__conjunto1 = ""
        self.__conjunto2 = ""

    def __obtenerLista(self, conjuntoCadena):

        conjunto = conjuntoCadena.strip().split(';')
        esDigito = True

        i = 0
        N = len(conjunto)
        while i < N and esDigito:

            esDigito = conjunto[i].isdigit()

            if esDigito:
                conjunto[i]
                i += 1
        result = esDigito and i == N and N != 0

        if not result:
            print("Error. No ingreso un conjunto valido.")
            conjunto.clear()
        return result, conjunto

    def crearConjuntos(self, conjunto_1, conjunto_2):

        conjunto1 = []
        conjunto2 = []
        exito, conjunto1 = self.__obtenerLista(conjunto_1)
        if exito:
            exito , conjunto2 = self.__obtenerLista(conjunto_2)

        if exito:
            self.__conjunto1 = Conjunto(conjunto1)
            self.__conjunto2 = Conjunto(conjunto2)
        return exito

   
    def __verUnion(self):
        print("{} + {} = {}".format(self.__conjunto1, self.__conjunto2, self.__conjunto1 + self.__conjunto2))
    
    def __verDiferencia(self):
        print("{} - {} = {}".format(self.__conjunto1, self.__conjunto2, self.__conjunto1 - self.__conjunto2))
    
    def __sonIguales(self):
        print("{} = {} ? {}".format(self.__conjunto1, self.__conjunto2, self.__conjunto1 == self.__conjunto2))

    def operaciones(self):


        seguir = True


        while seguir:

            print ("1 = Union")
            print ("2 = Diferencia")
            print ("3 = Ver igualdad")
            print("0 = Salir\n")

            opci = input().strip()

            if not opci.isdigit():
                print("Error. Debe ingresar un numero")

            elif opci == "0":
                print("Adios :)")
                seguir = False

            elif opci == '1':
                self.__verUnion()

            elif opci == '2':
                self.__verDiferencia()

            elif opci == '3':
                self.__sonIguales()
            else:
                print("Error. La eleccion no es valida.")


                