# Integrantes:
# - [Apellido Nombre]
# - [Apellido Nombre]
# - [Apellido Nombre]

class GestorBiblioteca:
    def __init__(self, nombre_biblioteca: str):
        self._nombre_biblioteca = nombre_biblioteca
        self._servicios = []

    @property
    def nombre_biblioteca(self):
        return self._nombre_biblioteca

    @nombre_biblioteca.setter
    def nombre_biblioteca(self, valor):
        if valor == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre_biblioteca = valor

    @property
    def servicios(self):
        return self._servicios

    def agregar_servicio(self, servicio):
        self._servicios.append(servicio)

    def calcular_costo_total(self):
        total = 0
        for servicio in self.servicios:
            total += servicio.calcular_costo()
        return total

    def generar_reporte(self):
        print(f"\n--- REPORTE: {self.nombre_biblioteca} ---")
        for servicio in self.servicios:
            print(servicio.mostrar_info())
        print("--- FIN ---")

    def __str__(self):
        return f"Gestor: {self.nombre_biblioteca} | Servicios: {len(self.servicios)}"