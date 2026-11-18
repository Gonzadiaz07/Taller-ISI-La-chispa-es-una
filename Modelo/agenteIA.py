from datetime import datetime 
from autor import Autor 
from gestorIA import GestorIA
from Pregunta import Pregunta
from Respuesta import Respuesta

class AgenteIA(Autor): #Se declara la clase AgenteIA y se le pone como parametro Autor, ya que la misma hereda informacion de esta ultima clase
    def __init__(
        self,
        id_autor: int,
        nombre: str,
        reputacion: int,
        versionModelo: str,
        gestorIA: GestorIA,
    ):
        # Inicializa los atributos heredados de Autor
        super().__init__(id_autor, nombre, reputacion) # Llama al constructor de la clase padre. 
        self._versionModelo = versionModelo # Guarda dentro del objeto el atributo propio de AgenteIA
        self._gestorIA = gestorIA # Guarda la referencia al GestorIA dentro del agente para vincularlos.

    def procesarGeneracionAutomatica(self, pregunta: Pregunta) -> Respuesta:
        #Le pide al GestorIA que redacte el texto para la pregunta construye el objeto Respuesta asociado
        texto_generado = self._gestorIA.redactarTexto(pregunta)

        nueva_respuesta = Respuesta(
            id_autor=0, # Se le asigna el valor de 0 hasta ser remplazado 
            cuerpo=texto_generado, # Texto redactado por la IA 
            fechaPublicacion=datetime.now(), # Fecha y hora que se genero
            autor=self, # 
        )
    #########
    def get_reputacion(self) -> int:
        return self._reputacion

    def procesarGeneracionAutomatica(self, pregunta: Pregunta) -> Respuesta:
        # Le pide al GestorIA que redacte el texto para la pregunta y construye el objeto Respuesta asociado
        texto_generado = self._gestorIA.redactarTexto(pregunta)

        nueva_respuesta = Respuesta(
            id=0,  # Se le asigna el valor de 0 hasta ser reemplazado
            cuerpo=texto_generado,  # Texto redactado por la IA
            fecha_publicacion=datetime.now().date(),  # Fecha en que se generó
            autor=self,
        )

        return nueva_respuesta