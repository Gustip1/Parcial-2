from claseautobuses import autobus
from clasevanes import vanes
import csv

class lista:
    __lista:list

    def __init__(self):
        self.__lista=[]

    def carga(self):
        archivo=open("vehiculos.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        next(reader)
        for fila in reader:
            if len(fila) == 10:
                nuevoautubous=autobus(fila[0],fila[1],(fila[2]),int(fila[3]),int(fila[4]),int(fila[5]),float(fila[6]),float(fila[7]),fila[8],fila[9])
                self.__lista.append(nuevoautubous)
            elif len(fila) == 9:
                nuevavan=vanes(fila[0],fila[1],(fila[2]),int(fila[3]),int(fila[4]),int(fila[5]),float(fila[6]),float(fila[7]),fila[8])
                self.__lista.append(nuevavan)
        archivo.close()

    def mostar(self):
        for vehiculo in self.__lista:
            print(vehiculo)

    def inciso2(self):
        pos=int(input("ingrese una posicion:"))
        while pos<0 or pos>=len(self.__lista):
            print("Poisicion fuera de rango, vuelva a intentar. ")
            pos=int(input("Ingrese posicion: "))
        if True:
            item=self.__lista[pos]
            if isinstance(item,autobus):
                 print(f"El vehiculo en la posicion {pos} es un autobus. \n")
            elif isinstance(item, vanes):
                print(f"El vehiculo en la posicion {pos} es una van. \n")
            else:
                print(f"La vehiculo en la posicion {pos} es de tipo desconocido. \n")

    def agregar(self):
        vehiculo = input("Ingrese el tipo de vehiculo, A para autobuses y V para vanes: ")
        m = input("Ingrese Marca: ") 
        s = input("Ingrese modelo:")  
        a = int(input("Ingrese año de fabricacion:"))
        b = int(input("Ingrese capacidad de pasajeros: "))
        c = int(input("Ingrese el numero de plazas:"))
        d = float(input("Ingrese la distancia recorrida:"))
        e = float(input("Ingrese la tarifa base:"))
        if vehiculo == "A":
            t = input("Ingrese un tipo de servicio:")
            l = input("Ingrese un tipo de turno")
            nuevobus = autobus(vehiculo,m, s, a, b, c, d, e, t, l)
            self.__lista.append(nuevobus)
            print("El vehiculo fue agregado exitosamente")
        elif vehiculo == "V":
            x = input("Ingrese el tipo de carroceria: ")
            nuevavan = vanes(vehiculo,m, s, a, b, c, d, e, x)
            self.__lista.append(nuevavan)
            print("El vehiculo fue agregado exitosamente")

    
    def muestra_vehiculos(self):
        contador=0
        contador1=0
        for i in range (len(self.__lista)):
            if isinstance (self.__lista[i],autobus):
                contador+=1
            elif isinstance (self.__lista[i],vanes):
                contador1+=1
        print (f"la cantidad de autobuses que hay es de {contador} y la cantidad de minivanes es de {contador1}")

    def mostrartodo(self):
        for vehiculo in self.__lista:
            print(vehiculo.mostrarinfo())

