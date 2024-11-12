#-----------------------------------ENTRADAS Y SALIDA DE DATOS----------------------------------
#-------------------------------¿Qué son los datos de entrada?---------------------------------- 
# Los datos de entrada son todos aquellos que son ingresados al sistema. Ya sea mediante el usuario, un sensor, archivos, bases de datos, etc. 
# Si un programa me pide que ingrese un número, el dato que yo ingrese sería considerado un dato de entrada.
#-------------------------------¿Qué son los datos de salida?-----------------------------------
# Son todos aquellos que salen del sistema, ya sea en consola, en pantalla, en una impresión, etc.
#Por ejemplo: Si hago la siguiente suma "2+2" y lo almaceno en una variable llamada resultada e imprimo esa variable, print(resultado), Mi dato de salida sería 4, que es el valor almacenado del resultado de la operación.

#----------------------------Ejemplo de dato de entrada-----------------------------------------
nombre = input("Ingresa tu nombre") #Este sería un dato de entrada, ya que lo que hace la función input() es permitirle al usuario ingresar un valor en consola.

#----------------------------Dato de salida----------------------------------------------------
print(nombre)#En esta variable almacenamos el nombre que nos ingrese el usuario, y vamos a imprimir el valor, en este caso estaríamos realizando un dato de salida.

#--------------------Ejercicio Suma de 2 numeros-----------------------------------------------
#Descripción, el usuario deberá de ingresar 2 números y el sistema realizará una suma y la mostrará en consola.
#Tenemos que especificar que tiene que ser un número entero, ya que de lo contrario concatenaría los valores y no los sumaría. 
#La función input por defecto almacena un valor de tipo cadena o string, esto ya que permite que el usuario ingrese cualquier tipo de carácter. Es por eso que si vamos a realizar una operación hay que especificar el tipo de dato o convertirlo.

#Le pedimos al usuario ingresar los 2 números y los almacenará en cada variable.
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))
resultado = numero1 + numero2 #Realizará una suma y este resultado lo almacenará en la variable llamada resultado.
print("Hola ",nombre, "tu resultado es: ", resultado)#Imprimimos el valor del resultado
#Utilizamos las comas para concatenar los valores y mandar un mensaje más amigable al usuario.
