
#Romero Martha

  #importemos cuenta y hagamos las pruebas de Cuenta
   from Cuenta import *


class Pruebas:

#significa que esta vacía
	pass

#definamos
print ("Veremos los productos: ")

cuenta1 = cuenta (800 ,"debito",' Café') 
cuenta2 = cuenta (400 ,"debito", ' Café')
cuenta3 = cuenta (1500 , "debito",'Chocolate')

 #probaremos que se lean los códigos
print(cuenta1.cantidad)
print(cuenta1.tipo)
print(cuenta1.color)
cuenta1.imprimirdetalles()


print(cuenta2.cantidad)
print(cuenta2,tipo)
print(cuenta2.color)
cuenta2.imprimirdetalles()

print(cuenta3.cantidad)
print(cuenta3.tipo)
print(cuenta3.color)
cuenta3.imprimirdetalles()


#probaremos con la clase cliente
     from Cliente import *
 

print ("CLIENTES: ")

#definamos las variables en clientes
cliente1 = cliente ("Juan Antonio Rodríguez", 6000)
cliente2 = cliente ("Miranda Velazquez", 1500)
cliente3 = CLiente ("Nathan Morales", 2500)

#coloquemos los comandos para que lea los códigos
print(cliente1.nombre)
print(cliente1.saldo)
cliente1.imprimirdetalles() 


print(cliente2.nombre)
print(cliente2.saldo)
cliente2.imprimirdetalles() 


print(cliente3.nombre)
print(cliente3.saldo)    
cliente3.imprimirdetalles() 


    #Ahora probaremos la clase Tienda con dos argumentos
      from Tienda import *

#definamos las tiendas 
tienda1 = tienda("Muebleria", "Silla")
tienda2 = tienda("Muebleria", "Mesa"
tienda3 = tienda("Muebleria", "Alacena")

#Coloquemos los comandos para que se lea Tienda
print (tienda1.nombre)
print(tienda1.producto)
tienda1.imprimirdetalles()

print (tienda2.nombre)
print (tienda2.producto)
tienda2.imprimirdetalles()

print (tienda3.nombre)
print (tienda3.producto)
tienda3.imprimirdetalles()
