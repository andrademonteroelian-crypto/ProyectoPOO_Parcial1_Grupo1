# Integrantes:
# - Juan Carlos
# - Jennifer Mazzini
# - Lisseth Zambrano
# - Elian Andrade
# - Nathaly Nacipucha

from servicio_biblioteca import ServicioBiblioteca

class PrestamoLibro(ServicioBiblioteca):
    COSTO_BASE = 5.0
    MULTA_POR_DIA = 2.0

    def __init__(self, codigo: str, titulo_recurso: str, fecha_prestamo: str, dias_prestamo: int, dias_atraso: int = 0):
        super().__init__(codigo, titulo_recurso, fecha_prestamo, dias_prestamo)
        self._dias_atraso = dias_atraso

    @property
    def dias_atraso(self):
        return self._dias_atraso

    @dias_atraso.setter
    def dias_atraso(self, valor):
        if valor < 0:
            raise ValueError("Los días de atraso no pueden ser negativos")
        self._dias_atraso = valor

    def calcular_costo(self):
        multa = self.dias_atraso * self.MULTA_POR_DIA
        return self.COSTO_BASE + multa

    def mostrar_info(self):
        costo = self.calcular_costo()
        return f"Préstamo Físico -> {super().__str__()} | Atraso: {self.dias_atraso} días | Costo: ${costo:.2f}"

    def __str__(self):
        return self.mostrar_info()
