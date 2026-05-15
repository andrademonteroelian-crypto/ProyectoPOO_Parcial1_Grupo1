# Integrantes:
# - [Apellido Nombre]
# - [Apellido Nombre]
# - [Apellido Nombre]

class UsuarioBiblioteca:
    def __init__(self, nombre: str, id_usuario: str, email: str):
        self._nombre = nombre
        self._id_usuario = id_usuario
        self._email = email

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, valor):
        if valor == "":
            raise ValueError("El ID no puede estar vacío")
        self._id_usuario = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if valor == "":
            raise ValueError("El email no puede estar vacío")
        self._email = valor

    def __str__(self):
        return f"Usuario: {self.nombre} | ID: {self.id_usuario} | Email: {self.email}"