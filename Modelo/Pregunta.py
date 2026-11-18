from datetime import date

class Pregunta: 
    def __init__(self, id: int, titulo: str, cuerpo: str, fecha_publicacion: date, categoria = None, autor = None):
        self._categoria = categoria
        self._autor = autor 
        self._respuestas = [] 
        self._etiquetas = []
        self._votos = [] 

    def asignar_categoria(self, categoria) -> None:
        self._categoria = categoria

    def agregar_respuesta(self, respuesta) -> None:
        self._respuestas.append(respuesta)

    def agregar_etiqueta(self, etiqueta) -> None:
        self._etiquetas.append(etiqueta)

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

    def tiene_etiqueta_ia(self) -> bool:
        for etiqueta in self._etiquetas:
            if etiqueta.get_nombre().upper() == "IA":
                return True
        return False 
