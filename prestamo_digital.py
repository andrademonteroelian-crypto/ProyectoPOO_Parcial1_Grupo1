# Integrantes:
# - Juan Carlos
# - Jennifer Mazzini
# - Lisseth Zambrano
# - Elian Andrade
# - Nathaly Nacipucha
# - Eylen Flores

from servicio_biblioteca import ServicioBiblioteca

class PrestamoDigital(ServicioBiblioteca):
    COSTO_POR_DIA_EBOOK = 1.5
    COSTO_POR_DIA_VIDEO = 3.0

    def __init__(self, codigo: str, titulo_recurso: str, fecha_prestamo: str, dias_prestamo: int, tipo_recurso: str = "ebook"):
        super().__init__(codigo, titulo_recurso, fecha_prestamo, dias_prestamo)
        self._tipo_recurso = tipo_recurso

    @property
    def tipo_recurso(self):
        return self._tipo_recurso

    @tipo_recurso.setter
    def tipo_recurso(self, valor):
        if valor not in ["ebook", "video"]:
            raise ValueError("El tipo debe ser 'ebook' o 'video'")
        self._tipo_recurso = valor

    def calcular_costo(self):
        if self.tipo_recurso == "ebook":
            return self.dias_prestamo * self.COSTO_POR_DIA_EBOOK
        return self.dias_prestamo * self.COSTO_POR_DIA_VIDEO

    def mostrar_info(self):
        costo = self.calcular_costo()
        return f"Préstamo Digital -> {super().__str__()} | Tipo: {self.tipo_recurso} | Costo: ${costo:.2f}"

    def __str__(self):
        return self.mostrar_info()
