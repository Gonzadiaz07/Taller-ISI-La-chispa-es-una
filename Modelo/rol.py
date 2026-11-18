class Rol:
    def __init__(self, id_rol: int, nombre: str, descripcion: str):
        self._id_rol = id_rol
        self._nombre = nombre
        self._descripcion = descripcion

    @property
    def nombre(self) -> str:
        return self._nombre

    def __str__(self) -> str:
        return f"Rol: {self._nombre}, {self._descripcion}"
