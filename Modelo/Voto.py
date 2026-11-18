from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Usuario import Usuario


class Voto:
    def __init__(self, id: int, es_positivo: bool, fecha_emision: date, votante: 'Usuario'):
        self._id = id
        self._es_positivo = es_positivo
        self._fecha_emision = fecha_emision
        self._votante = votante

    def es_positivo(self) -> bool:
        return self._es_positivo