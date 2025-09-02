# Programa para registrar viajes semanales en El Salvador

class Viaje:
    def _init_(self, ruta, costo, tiempo):
        self.ruta = ruta
        self.costo = costo
        self.tiempo = tiempo

    def mostrar(self):
        return f"Ruta: {self.ruta} | Costo: ${self.costo} | Tiempo: {self.tiempo} min"


# Lista para guardar los viajes
viajes = []

print("==== Registro de viajes semanales ====\n")
while True:
    ruta = input("Ingrese la ruta: ")
    costo = float(input("Ingrese el costo del viaje: "))
    tiempo = int(input("Ingrese el tiempo en minutos: "))

    viaje = Viaje(ruta, costo, tiempo)
    viajes.append(viaje)

    op = input("¿Desea registrar otro viaje? (s/n): ")
    if op.lower() != "s":
        break

# Mostrar viajes registrados
print("\n--- Viajes Registrados ---")
total_costo = 0
total_tiempo = 0
for v in viajes:
    print(v.mostrar())
    total_costo += v.costo
    total_tiempo += v.tiempo

print("\n--- Resumen ---")
print(f"Gasto total de la semana: ${total_costo}")
print(f"Tiempo total de la semana: {total_tiempo} minutos")