# Clase base
class Vehiculo:
    def __init__(self, matricula, num_ruedas):
        pass

    def get_matricula(self):
        pass

    def set_matricula(self, matricula):
        pass

    def get_num_ruedas(self):
        pass

    def set_num_ruedas(self, num_ruedas):
        pass

    def mostrar_informacion(self):
        print(f"Vehículo con matrícula {self.__matricula} y {self.__num_ruedas} ruedas")

# Clases derivadas
class Auto(Vehiculo):
    def __init__(self, matricula, num_ruedas, num_puertas):
        pass

    def mostrar_informacion(self):
        pass

class Moto(Vehiculo):
    def __init__(self, matricula, num_ruedas, tipo_manillar):
        pass

    def mostrar_informacion(self):
        pass

class Camion(Vehiculo):
    def __init__(self, matricula, num_ruedas, capacidad_carga):
        pass

    def mostrar_informacion(self):
        pass

# Clase derivada de Auto para vehículos eléctricos
class AutoElectrico(Auto):
    def __init__(self, matricula, num_ruedas, num_puertas, nivel_bateria):
        pass

    def mostrar_informacion(self):
        pass

    def get_nivel_bateria(self):
        pass

    def set_nivel_bateria(self, nivel_bateria):
        pass

# Pruebas de implementación
if __name__ == "__main__":
    auto = Auto("ABC123", 4, 4)
    moto = Moto("XYZ789", 2, "deportivo")
    camion = Camion("LMN456", 8, 15)
    auto_electrico = AutoElectrico("EFG123", 4, 4, 85)

    auto.mostrar_informacion()
    moto.mostrar_informacion()
    camion.mostrar_informacion()
    auto_electrico.mostrar_informacion()
