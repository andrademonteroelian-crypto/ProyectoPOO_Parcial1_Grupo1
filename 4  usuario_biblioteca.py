# Integrantes:
# - [ELIAN ANDRADE]
# - [TOALA MOSERRATE JUAN]
# - [NACIPUCHA SUAREZ NATHALY]
# - [FLORE LOPEZ EYLEN]
# - [ZAMBRANO CORREA LISSETH]
# - [MAZZINI ZAMBRANO JENNIFER]


class UsuarioBiblioteca:
    """
    Clase adicional que representa un usuario de la biblioteca.
    """

    def __init__(self, nombre, id_usuario, email):
        """Constructor que recibe y guarda los datos del usuario."""
        self._nombre = nombre          # Guarda el nombre del usuario (privado)
        self._id_usuario = id_usuario  # Guarda el ID único (privado)
        self._email = email            # Guarda el correo electrónico (privado)

    @property
    def nombre(self):
        """Devuelve el nombre guardado."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        """Valida que el nombre no esté vacío."""
        if valor == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor

    @property
    def id_usuario(self):
        """Devuelve el ID guardado."""
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, valor):
        """Valida que el ID no esté vacío."""
        if valor == "":
            raise ValueError("El ID no puede estar vacío")
        self._id_usuario = valor

    @property
    def email(self):
        """Devuelve el email guardado."""
        return self._email

    @email.setter
    def email(self, valor):
        """Valida que el email no esté vacío."""
        if valor == "":
            raise ValueError("El email no puede estar vacío")
        self._email = valor

    def __str__(self):
        """Devuelve string con los datos del usuario."""
        return f"Usuario: {self.nombre} | ID: {self.id_usuario} | Email: {self.email}"
