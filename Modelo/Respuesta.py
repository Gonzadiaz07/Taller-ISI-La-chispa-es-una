from datetime import date

class Respuesta:
    def __init__(self, id:int, cuerpo:str, fecha_publicacion: date, autor = None):
        self._esAceptada = False
        self._votos = []
        self._id = id
        self._cuerpo = cuerpo
        self._fecha_publicacion = fecha_publicacion
        self._autor = autor

    def marcar_como_aceptada(self) -> None:
        self._esAceptada = True

    def recibir_voto(self, voto) -> None:
        self._votos.append(voto) 

    def calcular_puntuacion_total(self) -> int:
        total = 0
        for voto in self._votos:
            if voto.es_positivo():
                total += 1
            else:
                total -= 1
        return total