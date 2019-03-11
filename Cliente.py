#Romero Martha


#Nombremos la clase como Cliente.
class cliente:


  #ahora definamo los parametro 
   def __init__(self,nombre, saldo):
     self.nombre = nombre
     self.saldo = saldo


  #acomdemos como se deben imprimir los argumentos que tenemos en el programa
    def imprimir detalles (self):
     print("desde el método")
     print("Nombre:  "self.nombre )
     print("Su saldo es:  ", self.saldo ) 
