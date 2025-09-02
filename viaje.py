# Clase para guardar la info de cada viaje
class Viaje:
    def init(self, ruta, costo, tiempo):
        self.ruta = ruta
        self.costo = costo
        self.tiempo = tiempo

    def mostrar(self):
        return f"Ruta: {self.ruta} | Costo: ${self.costo} | Tiempo: {self.tiempo} min"
from viaje import Viaje