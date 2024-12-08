#Clase representa el DTO para la creacion de factura
class FacturaDTO:
    def __init__(self,monto,nombre,apellido,dni,direccion):
        self.monto=monto
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.direccion=direccion
