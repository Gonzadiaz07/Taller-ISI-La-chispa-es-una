class Categoria:
    def __init__(self, id: int, nombre: str, descripcion: str):
        self._id = id
        self._nombre = nombre
        self._descripcion = descripcion

    def get_nombre(self) -> str:
        return self._nombre