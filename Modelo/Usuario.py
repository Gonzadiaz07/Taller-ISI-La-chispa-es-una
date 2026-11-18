from typing import TYPE_CHECKING #Constante boolean que indica si se está realizando una verificación de tipos en tiempo de ejecución. Se utiliza para evitar importaciones circulares y mejorar el rendimiento en tiempo de ejecución.
from Autor import Autor #Importamos la clase Autor desde el archivo autor.py.
from Rol import Rol #Importamos la clase Rol desde el archivo rol.py.

#Evita errores de importacion mientras se desarrollan las demas clases.
if TYPE_CHECKING:
    from Pregunta import Pregunta #Importamos la clase Pregunta desde el archivo pregunta.py.
    from Respuesta import Respuesta #Importamos la clase Respuesta desde el archivo respuesta.py.
    from Categoria import Categoria #Importamos la clase Categoria desde el archivo categoria.py.
    from Voto import Voto #Importamos la clase Voto desde el archivo voto.py.

class Usuario(Autor): #Definimos la clase Usuario que hereda de la clase Autor.
    def __init__(self, id_Autor: int, nombre: str, email:str, contraseña: str, rol: Rol, reputacion: int = 0): #Definimos el constructor de la clase Usuario con sus atributos.
        super().__init__(id_Autor, nombre, reputacion) #Llamamos al constructor de la clase padre Autor.
        self._email = email
        self._contraseña = contraseña
        self._rol = rol

    #Implementacion del metodo abstracto get_reputacion de la clase Autor.
    def get_reputacion(self) -> int: 
        return self._reputacion

    #Logica de inicio de sesion
    def iniciar_sesion(self, email: str, contraseña: str) -> bool: #Metodo que permite iniciar sesion en la aplicacion.
        return self._email == email and self._contraseña == contraseña #Retorna True si el email y la contraseña coinciden con los del usuario, de lo contrario retorna False.

    #Metodos que conectan con los modulos 2 y 3
    def publicar_pregunta(self, titulo: str, cuerpo: str, categoria: 'Categoria') -> 'Pregunta': #Metodo que permite publicar una pregunta en la aplicacion.
        nueva_pregunta= Pregunta(titulo=titulo, cuerpo=cuerpo, categoria=categoria, autor=self) #Creamos una nueva instancia de la clase Pregunta con los parametros recibidos.
        return nueva_pregunta #Retornamos la nueva pregunta creada.
    
    def publicar_respuesta(self, pregunta: 'Pregunta', cuerpo: str) -> 'Respuesta':
        nueva_respuesta = Respuesta(cuerpo=cuerpo, autor=self) #Creamos una nueva instancia de la clase Respuesta con los parametros recibidos.
        pregunta.agregar_respuesta(nueva_respuesta) #Agregamos la nueva respuesta a la pregunta correspondiente.
        return nueva_respuesta #Retornamos la nueva respuesta creada.

    def aceptar_respuesta(self, respuesta: 'Respuesta') -> None:
        respuesta.marcar_como_aceptada()

    def votar(self, elemento_id: int, es_positivo: bool) -> 'Voto':
       nuevo_voto = Voto(es_positivo=es_positivo, votante=self) #Creamos una nueva instancia de la clase Voto con los parametros recibidos.
       return nuevo_voto #Retornamos el nuevo voto creado.