from estrategiaLLM import EstrategiaLLM
from pregunta import Pregunta


class GestorIA:
    def __init__(self, estrategiaActual: EstrategiaLLM):
        self._estrategiaActual = estrategiaActual

    # Nos permite cambiar de IA 
    def setEstrategia(self, estrategia: EstrategiaLLM) -> None:
        self._estrategiaActual = estrategia

    # Arma el contexto a partir de la pregunta y le delega la generacion a la estrategia de IA que este activa en ese momento.
    def redactarTexto(self, pregunta: Pregunta) -> str:
        if self._estrategiaActual is None:
            raise ValueError("No hay una estrategia de IA configurada.")

        # Armamos el texto de contexto con los datos de la pregunta
        contexto = f"Título: {pregunta._titulo}\nDetalle: {pregunta._cuerpo}"

        return self._estrategiaActual.generarRespuesta(contexto)