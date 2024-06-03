from clasegestor import lista
class unmenu:
    def __init__(self):
        self.GL=lista()

    def run(self):
        while True:
            a = input("""MENU DE OPCIONES
                    1 para hacer carga:
                    2 para hacer el item a 
                    3 para hacer el item b
                    4 para hacer el item c
                    5 para salir
                        """)
            if a == '1':
                self.GL.carga()
                self.GL.agregar()
                self.GL.mostar()
                
            if a == '2':
                self.GL.inciso2()
            if a == '3':
                self.GL.muestra_vehiculos()
            if a =='4':
                self.GL.mostrartodo()
            if a =='5':
                break