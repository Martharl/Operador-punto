#Romero Martha

#Nombremos la clase como cuenta.
class cuenta:

  #ahora definamos los parametros
   def __init__(self,valor,debito,color):
     
     self.cantida = valor
     self.tipo = debito
     self.color =color

  #coloquemos un condicional
   def deposiar(self,valor):
      if  valor > 0:
        self.cantidad= self.cantidad + valor
      else:
        print ("El valor para despositar es erroneo:")


  #organicemos como queremo que lo desmueatre el programa
    def imprimirdetalles (self):
     
     #ahora coloquemos para que el código se lea con sus diferentes argumentos
     print("La producto  es : "self.producto )
     print("Cuesta: ", self.costo ) 
     print("El color es: ", self.color)
     imprimirdetalles()
