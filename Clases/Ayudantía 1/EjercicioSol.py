# Clase base
class Vehiculo:
    def __init__(self, matricula, num_ruedas):
        self.__matricula = matricula  # Atributo privado
        self.__num_ruedas = num_ruedas  # Atributo privado

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_num_ruedas(self):
        return self.__num_ruedas

    def set_num_ruedas(self, num_ruedas):
        self.__num_ruedas = num_ruedas

    def mostrar_informacion(self):
        print(f"Vehículo con matrícula {self.__matricula} y {self.__num_ruedas} ruedas")

# Clases derivadas
class Auto(Vehiculo):
    def __init__(self, matricula, num_ruedas, num_puertas):
        super().__init__(matricula, num_ruedas)
        self.num_puertas = num_puertas

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Es un auto con {self.num_puertas} puertas")

class Moto(Vehiculo):
    def __init__(self, matricula, num_ruedas, tipo_manillar):
        super().__init__(matricula, num_ruedas)
        self.tipo_manillar = tipo_manillar

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Es una moto con manillar tipo {self.tipo_manillar}")

class Camion(Vehiculo):
    def __init__(self, matricula, num_ruedas, capacidad_carga):
        super().__init__(matricula, num_ruedas)
        self.capacidad_carga = capacidad_carga

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Es un camión con capacidad de carga de {self.capacidad_carga} toneladas")

# Clase derivada de Auto para vehículos eléctricos
class AutoElectrico(Auto):
    def __init__(self, matricula, num_ruedas, num_puertas, nivel_bateria):
        super().__init__(matricula, num_ruedas, num_puertas)
        self.__nivel_bateria = nivel_bateria  # Atributo privado

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Nivel de batería: {self.__nivel_bateria}%")

    def get_nivel_bateria(self):
        return self.__nivel_bateria

    def set_nivel_bateria(self, nivel_bateria):
        self.__nivel_bateria = nivel_bateria

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
