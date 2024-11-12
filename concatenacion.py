#-----------------------Maneras de concatenar---------------------------
#Se pueden concatenar de distintas maneras, ya que se puede utilizar una coma "," un más "+", o una interpolación con la letra f y sus respectivas llaves {}

#-------------------Concatenación con el operador de +------------------
cadena1 = "Hola"
cadena2 = "Mundo"
resultado = cadena1 + " " + cadena2  # "Hola Mundo"
print(resultado)
#------------------Concatenación con la coma ","------------------------
cadena1 = "Hola"
cadena2 = "Mundo"
print(cadena1, cadena2) #Hola mundo

#----------------Concatenación de interpolación con la letra f-----------
nombre = "Mundo"
print(f"Hola {nombre}")