class Conjunto:
	__conjunto : int 

	def __init__(self, conjunto):
		self.__conjunto = conjunto
		
		self.__eliminarRepetidos()


	def __eliminarRepetidos(self):

        
		unicos = [ ]
		for elemento in self.__conjunto:
			if not elemento in unicos:
				unicos.append(elemento)
		unicos.sort()
		self.__conjunto.clear()
		self.__conjunto = unicos


	def __str__(self):
		return str(self.__conjunto)
				
	def __add__(self, otro):
		union = None
		if type(self) == type(otro):
			union = list(self.__conjunto)
			for elemento in otro.__conjunto:
				if not elemento in union:
					union.append(elemento)
		return union


	def __sub__(self, otro):

		diferencia = None
		if type(self) == type(otro):
			diferencia = list(self.__conjunto)
			for eliminar in otro.__conjunto:
				if eliminar in diferencia:
					diferencia.pop(diferencia.index(eliminar))
		return diferencia


	def __eq__(self, otro):
		igualdad = None
		if type(self) == type(otro):
			return self.__conjunto == otro.__conjunto

			