#Ya conocemos como funcionan las condicionales, pero ¿Qué podemos hacer con ellas?
#La sentencia o condicional if elif y else son una condicional que se traduce como: si (if) mis calificaciones son mayores a 9 me van a comprar un celular, "pero si no" (elif) saco 9, pero saco 8 me van a comprar una tarjeta de regalo, "en caso de que mis calificaciones no sean mayores" (else) a un promedio de 8 no me van a regalar nada.
#if si se cumple la condición realiza esta acción.
#elif si la prime condición no se cumplió evalúa esta otra condición
#else si ninguna condición se cumplió entonces mándale un mensaje de que no se cumplió ninguna condición

#-------------------------------EJERCICIO DE CLASE ------------------------------------
#Deberas escribir un programa que te pida las calificaciones de tus 3 parciales, deberás sacar el promedio y evaluar si tengo promedio igual o mayor a 9, si tengo promedio igual o mayor a 8, y si no cumplo con ningún requisito.
#Solucion

#Le pedimos al usuario que ingrese sus calificaciones:
califiacion1 = float(input("Ingresa tu primer calificacion: "))
califiacion2 = float(input("Ingresa tu segunda calificacion: "))
califiacion3 = float(input("Ingresa tu tercera calificacion: "))

#Realizamos la operacion del promedio
promedio = (califiacion1 + califiacion2 + califiacion3)/3

#Operadores lógicos and y or estos sirven para evaluar dos condiciones
#and se tienen que cumplir las 2 o más condiciones como verdaderas para que pueda realizar la acción
#or con que se cumpla una de las condiciones se ejecuta la acción sin importar si las otras condiciones arrojaron un valor falso o false
#not devuelve lo contrario del resultado, True si es Falso y viceversa
if promedio >= 9 and promedio <= 10: #Evaluamos que el promedio sea igual o mayor a 9 Y (and) sea menor o igual a 10
  print("Felicidades te comprarán un celular. Tu promedio fue: ", promedio)
elif promedio >= 8 and promedio < 9: #Evaluamos que el promedio sea igual o mayor a 8, pero sea menor a 9 
  print("Felicidades te van a regalar un videojuego, pero hay que seguir esforzándose más.Tu promedio fue: ", promedio)
else: #Si no se cumple ninguna de esas condiciones (En este caso no cumple con el promedio)
  print("Esfuérzate más, en esta ocasión no hay recompensa por buenas calificaciones. Tu promedio fue:", promedio)