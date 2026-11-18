from abc import ABC, abstractmethod #ABC define la clase abstracta desde la base de python.

class Autor(ABC): ##Definimos la clase Autor abstracta con sus atributos.
    def __init__(self, id_autor: int, nombre: str, reputacion: int = 0):
        self._id_autor = id_autor
        self._nombre = nombre
        self._reputacion = reputacion

    def get_nombre(self) -> str: #Metodo que devuelve el nombre del autor.
        return self._nombre

    @abstractmethod
    def get_reputacion(self) -> int: #Metodo abstracto que devuelve la reputacion del autor.
        pass
