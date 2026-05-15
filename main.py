# Integrantes:
# - Juan Carlos
# - Jennifer Mazzini
# - Lisseth Zambrano
# - Elian Andrade
# - Nathaly Nacipucha

from usuario_biblioteca import UsuarioBiblioteca
from gestor_biblioteca import GestorBiblioteca
from prestamo_libro import PrestamoLibro
from prestamo_digital import PrestamoDigital

if __name__ == '__main__':
    usuario = UsuarioBiblioteca("Ana García", "U001", "ana@email.com")
    print("=" * 50)
    print(usuario)
    print("=" * 50)

    gestor = GestorBiblioteca("Biblioteca Central")
    print(f"\n{gestor}")

    prestamo_fisico = PrestamoLibro("P001", "Python Básico", "2024-01-10", 7, 3)
    prestamo_digital1 = PrestamoDigital("P002", "Data Science", "2024-01-15", 10, "ebook")
    prestamo_digital2 = PrestamoDigital("P003", "Curso POO", "2024-01-20", 5, "video")

    gestor.agregar_servicio(prestamo_fisico)
    gestor.agregar_servicio(prestamo_digital1)
    gestor.agregar_servicio(prestamo_digital2)

    print(f"\nServicios: {len(gestor.servicios)}")

    print("\n=== INFO DE CADA SERVICIO ===")
    for servicio in gestor.servicios:
        print(servicio)
        print("-" * 40)

    print("\n=== POLIMORFISMO 1: COSTO TOTAL ===")
    total = gestor.calcular_costo_total()
    print(f"Total: ${total:.2f}")

    print("\n=== POLIMORFISMO 2: REPORTE ===")
    gestor.generar_reporte()

    print("\n=== VALIDACIÓN ===")
    try:
        prestamo_fisico.codigo = ""
    except ValueError as e:
        print("Error:", e)

    try:
        prestamo_digital1.dias_prestamo = -5
    except ValueError as e:
        print("Error:", e)
