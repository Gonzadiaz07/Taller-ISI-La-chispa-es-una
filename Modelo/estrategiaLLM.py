from abc import ABC, abstractmethod


class EstrategiaLLM(ABC):
    @abstractmethod
    def generarRespuesta(self, contexto: str) -> str:
        pass