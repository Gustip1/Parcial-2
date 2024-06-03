class vehiculo:
    __tipo_vehiculo:str
    __marca:str 
    __modelo:str 
    __año_de_fabricacion:int 
    __capacidad_de_pasajeros:int
    __numero_de_plazas:int
    __distancia_recorrida:float
    __tarifa_base:float
    
    def __init__(self,tipo_vehiculo,marca,modelo,año_fab,capacidad,numero_de_plazas,distancia,tarifa_base):
        self.__tipo_vehiculo=tipo_vehiculo
        self.__marca=marca
        self.__modelo=modelo
        self.__año_de_fabricacion=año_fab
        self.__capacidad_de_pasajeros=capacidad
        self.__numero_de_plazas=numero_de_plazas
        self.__distancia_recorrida=distancia
        self.__tarifa_base=tarifa_base
    
    def get_tipo_vehiculo(self):
        return self.__tipo_vehiculo

    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def get_año_fabricacion(self):
        return self.__año_de_fabricacion
    def get_capacidad(self):
        return self.__capacidad_de_pasajeros
    def get_numero_plazas(self):
        return self.__numero_de_plazas
    def get_distancia_recorrida(self):
        return self.__distancia_recorrida
    def get_tarifa_base(self):
        return self.__tarifa_base
    def mostrarinfo(self):
        return (f"Modelo:{self.__modelo}, Año:{self.__año_de_fabricacion}, Capacidad:{self.__capacidad_de_pasajeros}, Tarifa:{self.__tarifa_base}")
    def __str__(self):
        return f"Tipo vehiculo: {self.__tipo_vehiculo} Marca: {self.__marca}, Modelo: {self.__modelo}, Año de fabricacion: {self.__año_de_fabricacion}, Capacidad: {self.__capacidad_de_pasajeros}, Numero de Plazas {self.__numero_de_plazas}, Distancia recorrida {self.__distancia_recorrida}, Tarifa Base: {self.__tarifa_base}  "
    