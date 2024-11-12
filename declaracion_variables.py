#-----------------REGLAS PARA DECLARAR VARIABLES----------------------------------------------
#Reglas que hay que considerar para tener buenas prácticas al declarar variables
#1. El nombre de la variable debe de estar compuesto por MAYÚSCULAS, minúsculas, dígitos, y el carácter _ (guion bajo) NOTA: El carácter guion bajo es considerado una letra.
#2. Deben de comenzar con una letra (a-z) NOTA: también se puede con letras mayúsculas(A-Z), pero se recomienda utilizar mayúsculas cuando se va a declarar una función. 
#3. Las mayúsculas y minúsculas se tratan de forma distinta. Alicia y ALICIA son el mismo nombre, pero en Python son dos nombres de variable distintos, subsecuentemente, son dos variables diferentes;
#4. El nombre de las variables no pueden ser igual a alguna de las palabras reservadas de Python 
#5. No se pueden utilizar palabras reservadas para declarar variables (False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield)

#---------------------------¿Qué es una variable?---------------------------------------------
#En pocas palabras podemos ver una variable como un contenedor que dentro de ella almacenara un valor.
#-------------------------Ejemplos correctos de declarar variables----------------------------
#Formas correctas para declarar variables:
#MiVariable
#i
#t34
#apellido_paterno
#contador
#dias_para_navidad
#TheNameIsTooLongAndHardlyReadable
#_
#Nota: Python te permite usar no solo letras latinas, sino también caracteres específicos de idiomas que usan otros alfabetos.
#adiós_Señora
#sûr_la_mer
#einbahnstraße
#переменная
#-------------------------Ejemplos incorrectos de declarar variables--------------------------
#Formas incorrectas de declarar una variable:
#10t (no comienza con una letra)
#&important (no comienza con una letra)
#exchange rate (contiene un espacio).

#-----------------------Ejemplos de variables y su tipo de dato:------------------------------

entero = 10 #Sabemos que es un número entero porque no contiene punto decimal.
flotante = 10.0 #Sabemos que es flotante porque tiene punto decimal
cadena = "Hola mundo"#Sabemos que es cadena porque está entre comillas.
booleano = True #Sabemos que es boolean porque contiene como valor las palabras reservadas True o False.
lista = ["Hola mundo", 0, 1.0, True, "0"] #Sabemos que es una lista porque está entre corchetes
#-------------------------Invocación de variables----------------------------------------------
#Para llamar una variable en Python y que se muestre en consola utilizamos la función print()

print(entero)
print(flotante)
print(cadena)
print(booleano)
print(list)

#Esto debera imprimir el contenido o valor que se almacena en las variables.

#--------------------------Tipo de dato---------------------------------------------------------
#¿Cómo podemos verificar su tipo de dato? Esto lo podemos hacer con la función type(). Esta función devolverá en la consola el tipo de dato que se almacena en la variable.

print(type(entero))
print(type(flotante))
print(type(cadena))
print(type(booleano))
print(type(lista))
