from datetime import date

class Voto:
    # Definicion inicial de la clase Voto con sus atributos
    def __init__(self, id:int, es_positivo:bool, fecha_emision:date, votante ):
        self._id = id
        self._es_positivo = es_positivo
        self._fecha_emision= fecha_emision
        self._votante = votante 

    # Returna el atributo es_positivo 
    def es_positivo(self) -> bool:
        return self._es_positivo

if __name__ == "__main__":
    voto_prueba = Voto(1, True, date.today(), "UsuarioDePrueba")
    print("¿Es positivo?:", voto_prueba.es_positivo())