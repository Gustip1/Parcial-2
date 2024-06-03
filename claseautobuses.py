from clasevehiculo import vehiculo
class autobus(vehiculo):
    __tipo_servicio: str
    __turno:str

    def __init__(self,tipo_vehiculo,marca,modelo,año_fab,capacidad,numero_de_plazas,distancia,tarifa_base,tipo_servicio,turno):
        super().__init__(tipo_vehiculo,marca,modelo,año_fab,capacidad,numero_de_plazas,distancia,tarifa_base)
        self.__tipo_servicio=tipo_servicio
        self.__turno=turno

    def get_servicio(self):
        return self.__tipo_servicio
    def get_turno(self):
        return self.__turno
    
    def get_tarifa_autobuses(self):
        if self.__turno == 'nocturno' and self.__tipo_servicio == 'turismo':
            return (self.get_tarifa_base() *1.20)
        else:
            return (self.get_tarifa_base() *1.05)

    def __str__(self):
        return f"Tipo vehiculo {self.get_tipo_vehiculo()} Marca: {self.get_marca()}, Modelo: {self.get_modelo()}, Año de fabricacion: {self.get_año_fabricacion()}, Capacidad: {self.get_capacidad()}, Numero de Plazas {self.get_numero_plazas()}, Distancia recorrida {self.get_distancia_recorrida()}, Tarifa Base: {self.get_tarifa_autobuses()}, Tipo de servicio: {self.__tipo_servicio}, Turno: {self.__turno}  "