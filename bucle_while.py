#--------------------------------------Bucle while---------------------------------------
#El bucle while se traduce como: mientras pase esto, tú no dejes de realizar esa acción
#Por ejemplo, mientras no llegues a la meta no dejes de dar pasos.
#-------------------------------------Ejemplo--------------------------------------------
# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

numeros_pares = 0
numeros_impares = 0
 
# Lee el primer número.
numero = int(input("Introduce un número o escribe 0 para detener: "))
 
# 0 termina la ejecución.
while numero != 0:
    # Verificar si el número es impar.
    if numero % 2 == 1:
        # Incrementar el contador de números impares.
        numeros_impares += 1
    else:
        # Incrementar el contador de números pares.
        numeros_pares += 1
    # Leer el siguiente número.
    numero = int(input("Introduce un número o escribe 0 para detener: "))
 
# Imprimir resultados.
print("Conteo de números impares:", numeros_impares)
print("Conteo de números pares:", numeros_pares)

#Como podemos ver, el while es un bucle que no tiene punto de detención, no se sabe cuantas veces se va a ejecutar, mientras la condición sea verdadera se seguirá ejecutando, pero de igual forma podemos hacer que se ejecute un número determinado de veces. 

contador = 0

while contador < 5: #Mientras el contador sea menor a 5
    contador +=1 #Se le suma una unidad al contador
    print("El bucle a recorrido ",contador)#Se imprime cada vez que se ejecuta el bucle
print("Ultima vuelta", contador)#Si únicamente quisiéramos saber el resultado, deberíamos imprimir la variable fuera del ciclo.

#NOTA: El "while True" no es un bucle en conjunto, estamos evaluando la condición del while como verdadera (True), en otras palabras estamos forzando a que entre al bucle, pero no estamos evaluando ninguna variable ni condición. Es por eso que requerimos de un break que rompa el bucle. Es por eso que se considera una mala práctica realizar evaluar un bucle while como verdadero (while True)
while True:
    print("hola")
    break