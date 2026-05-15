# Integrantes:
# - [Apellido Nombre]
# - [Apellido Nombre]
# - [Apellido Nombre]

class ServicioBiblioteca:
    def __init__(self, codigo: str, titulo_recurso: str, fecha_prestamo: str, dias_prestamo: int):
        self._codigo = codigo
        self._titulo_recurso = titulo_recurso
        self._fecha_prestamo = fecha_prestamo
        self._dias_prestamo = dias_prestamo

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor == "":
            raise ValueError("El código no puede estar vacío")
        self._codigo = valor

    @property
    def titulo_recurso(self):
        return self._titulo_recurso

    @titulo_recurso.setter
    def titulo_recurso(self, valor):
        if valor == "":
            raise ValueError("El título no puede estar vacío")
        self._titulo_recurso = valor

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @fecha_prestamo.setter
    def fecha_prestamo(self, valor):
        self._fecha_prestamo = valor

    @property
    def dias_prestamo(self):
        return self._dias_prestamo

    @dias_prestamo.setter
    def dias_prestamo(self, valor):
        if valor <= 0:
            raise ValueError("Los días deben ser mayores a cero")
        self._dias_prestamo = valor

    def calcular_costo(self):
        raise NotImplementedError("Debe implementarse en la subclase")

    def mostrar_info(self):
        raise NotImplementedError("Debe implementarse en la subclase")

    def __str__(self):
        return f"Código: {self.codigo} | Título: {self.titulo_recurso} | Fecha: {self.fecha_prestamo} | Días: {self.dias_prestamo}"