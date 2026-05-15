CodePreview

# Proyecto POO - Parcial 1

## Grupo 1: Sistema de Gestión de Servicios de Biblioteca

### Integrantes

- Juan Carlos
- Jennifer Mazzini
- Lisseth Zambrano
- Elian Andrade
- Nathaly Nacipucha
- Eylen Flores
  
### Descripción

Sistema que gestiona préstamos de biblioteca aplicando encapsulamiento,

herencia y polimorfismo.

### Diagrama de clases

ServicioBiblioteca (superclase) ├── PrestamoLibro (hija) └── PrestamoDigital (hija)

UsuarioBiblioteca (adicional) GestorBiblioteca (adicional, contiene los 2 métodos 

polimórficos)

plain

Copy

### Cómo ejecutar

Evidencias

[Capturas de pantalla aquí]

Video explicativo

[Enlace a YouTube o Drive con permisos de visualización]

### Diagrama de clases
ServicioBiblioteca (superclase)
├── PrestamoLibro (hija) → multa por días de atraso
└── PrestamoDigital (hija) → costo por tipo de recurso
UsuarioBiblioteca (adicional)
GestorBiblioteca (adicional) → 2 métodos polimórficos
plain
Copy

**Herencia:** Las hijas heredan de `ServicioBiblioteca` con `super()`.

**Polimorfismo:** `GestorBiblioteca` recorre la lista de servicios y ejecuta métodos comunes sin saber el tipo.
2. Guardar y subir a GitHub


git add README.md
git commit -m "Agregado diagrama de clases"
git push origin main
