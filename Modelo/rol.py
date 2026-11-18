class Rol:
    def __init__(self, id_rol: int, nombre: str, descripcion: str): #Definimos la clase Rol con sus atributos.
        self._id_rol = id_rol
        self._nombre = nombre
        self._descripcion = descripcion

    @property #permite gestionar el acceso a los atributos de una clase como si fueran atributos normales, pero ejecutando lógica interna al leerlos, modificarlos o eliminarlos.
    def nombre(self) -> str: #Metodo que retorna el nombre del rol.
        return self._nombre

    def __str__(self) -> str: #Metodo que devuelve una representacion en cadena del objeto Rol.
        return f"Rol: {self._nombre}, {self._descripcion}"
