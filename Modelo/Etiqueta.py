class Etiqueta:
    def __init__(self, id: int, nombre: str):
        self._id = id
        self._nombre = nombre

    def get_nombre(self) -> str:
        return self._nombre