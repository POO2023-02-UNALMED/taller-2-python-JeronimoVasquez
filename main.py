class Asiento:
    def __init__(self, color, precio, registro):
        self.precio = precio
        self.registro = registro
        self.color = color
    
    def cambiarColor(self, color):
        if color == "rojo":
            self.color = color
        elif color == "verde":
            self.color = color
        elif color == "amarillo":
            self.color = color
        elif color == "negro":
            self.color = color
        elif color == "blanco":
            self.color = color
        else: 
            self.color = self.color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):

        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, numero_registro):
        self.registro =  numero_registro
    
    def asignarTipo(self, tipo):
        if tipo == "electrico":
            self.tipo = tipo
        elif tipo == "gasolina":
            self.tipo = tipo
        else:
            self.tipo = self.tipo


class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = []
        self.marca = marca
        self.motor = motor
        self.registro = registro
    

    def cantidadAsientos(self):

        contador = 0
        
        for asiento in self.asientos:
            if asiento != None:
                contador +=1
        
        return contador
    

    def verificarIntegridad(self):

        if self.registro == self.motor.registro:

            contador = 0

            for asiento in self.asientos:
                if asiento != None:
                    if asiento.registro == self.registro and asiento.registro == self.motor.registro:
                        contador +=1
            
            if contador == self.cantidadAsientos():
                return "Auto original"
            else:
                return "Las piezas no son originales"
            
        
        else:
            return "Las piezas no son originales"
                    



        

        


        