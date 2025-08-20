class Animal:
    def __init__(self, nombre, peso, propietario, fecha_cumpleaños, fecha_ultima_vacuna):
        self._nombre = nombre
        self._peso = peso
        self._propietario = propietario
        self._fecha_cumpleaños = fecha_cumpleaños
        self._fecha_ultima_vacuna = fecha_ultima_vacuna

  
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

  
    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, valor):
        if valor > 0:
            self._peso = valor
        else:
            raise ValueError("El peso debe ser mayor que 0")


    @property
    def propietario(self):
        return self._propietario

    @propietario.setter
    def propietario(self, valor):
        self._propietario = valor

   
    @property
    def fecha_cumpleaños(self):
        return self._fecha_cumpleaños

    @fecha_cumpleaños.setter
    def fecha_cumpleaños(self, valor):
        self._fecha_cumpleaños = valor

 
    @property
    def fecha_ultima_vacuna(self):
        return self._fecha_ultima_vacuna

    @fecha_ultima_vacuna.setter
    def fecha_ultima_vacuna(self, valor):
        self._fecha_ultima_vacuna = valor
