from clasevehiculo import vehiculo
class vanes(vehiculo):
    __tipo_de_carroceria:str

    def __init__(self,tipo_vehiculo,marca,modelo,año_fab,capacidad,numero_de_plazas,distancia,tarifa_base,tipo_carroceria):
        super().__init__(tipo_vehiculo,marca,modelo,año_fab,capacidad,numero_de_plazas,distancia,tarifa_base)
        self.__tipo_de_carroceria=tipo_carroceria

    def get_carroceria(self):
        return self.__tipo_de_carroceria
    

    def get_tarifa_vanes(self):
        if self.__tipo_de_carroceria == 'minivan':
            return (self.get_tarifa_base() *0.9)
        else:
            return (self.get_tarifa_base() *1.025)


    def __str__(self):
         return f" Tipo vehiculo {self.get_tipo_vehiculo()} Marca: {self.get_marca()}, Modelo: {self.get_modelo()}, Año de fabricacion: {self.get_año_fabricacion()}, Capacidad: {self.get_capacidad()}, Numero de Plazas {self.get_numero_plazas()}, Distancia recorrida {self.get_distancia_recorrida()}, Tarifa Base: {self.get_tarifa_vanes()}, Tipo de carroceria {self.__tipo_de_carroceria}  "
