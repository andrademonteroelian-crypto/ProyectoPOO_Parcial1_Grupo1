# Integrantes:
# - [ELIAN ANDRADE]
# - [TOALA MOSERRATE JUAN]
# - [NACIPUCHA SUAREZ NATHALY]
# - [FLORE LOPEZ EYLEN]
# - [ZAMBRANO CORREA LISSETH]
# - [MAZZINI ZAMBRANO JENNIFER]

from usuario_biblioteca import UsuarioBiblioteca
from gestor_biblioteca import GestorBiblioteca
from prestamo_libro import PrestamoLibro
from prestamo_digital import PrestamoDigital


if __name__ == '__main__':
    """Programa principal que demuestra el funcionamiento completo del sistema."""

    # Muestra el encabezado del sistema
    print("=" * 50)
    print("SISTEMA DE BIBLIOTECA - GRUPO 1")
    print("=" * 50)

    # Crea un usuario de la biblioteca
    usuario = UsuarioBiblioteca("Ana García", "U001", "ana@email.com")
    print(f"\n{usuario}")  # Muestra los datos del usuario

    # Crea el gestor de la biblioteca
    gestor = GestorBiblioteca("Biblioteca Central")
    print(f"\n{gestor}")  # Muestra los datos del gestor

    # Crea tres préstamos de diferentes tipos
    prestamo_fisico = PrestamoLibro("P001", "Python Básico", "2024-01-10", 7, 3)
    prestamo_digital1 = PrestamoDigital("P002", "Data Science", "2024-01-15", 10, "ebook")
    prestamo_digital2 = PrestamoDigital("P003", "Curso POO", "2024-01-20", 5, "video")

    # Agrega los 3 préstamos a la lista del gestor (lista de la superclase)
    gestor.agregar_servicio(prestamo_fisico)
    gestor.agregar_servicio(prestamo_digital1)
    gestor.agregar_servicio(prestamo_digital2)

    print(f"\nServicios registrados: {len(gestor.servicios)}")

    # Muestra la información de cada servicio
    print("\n=== INFORMACIÓN DE CADA SERVICIO ===")
    for servicio in gestor.servicios:  # Recorre la lista de servicios
        print(servicio)  # Muestra los datos y costo del servicio actual
        print("-" * 40)

    # Ejecuta el método polimórfico 1: calcula el costo total de todos los servicios
    print("\n=== POLIMORFISMO 1: COSTO TOTAL ===")
    total = gestor.calcular_costo_total()
    print(f"Costo total de todos los servicios: ${total:.2f}")

    # Ejecuta el método polimórfico 2: genera reporte con info de todos
    print("\n=== POLIMORFISMO 2: REPORTE ===")
    gestor.generar_reporte()

    # Prueba de validaciones: intenta guardar datos incorrectos
    print("\n=== PRUEBA DE VALIDACIÓN ===")
    try:
        prestamo_fisico.codigo = ""  # Intenta poner código vacío (debe lanzar error)
    except ValueError as e:
        print(f"Error detectado: {e}")  # Captura y muestra el error

    try:
        prestamo_digital1.dias_prestamo = -5  # Intenta poner días negativos (debe lanzar error)
    except ValueError as e:
        print(f"Error detectado: {e}")  # Captura y muestra el error
