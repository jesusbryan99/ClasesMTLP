#En toda la lógica de programación continuamente crearemos condicionales, las cual evaluaremos como verdaderas o falsas (True o false). En la programación como en la vida estamos condicionando ciertas acciones o situaciones. 
#Por ejemplo: Si le pido a mis padres permiso para ir a una fiesta y la respuesta es igual a (==) si (verdadero o True) podre ir y si la respuesta es igual a no (Falso o False) no podre ir.

#---------------------------------Evaluando condiciones---------------------------------
#NOTA: en el print() podemos realizar operaciones y evaluar condiciones, aquí lo estamos utilizando como ejemplo para mostrar el resultado que devuelve una condición, verdadero o falso (True o False)
print(2==2) #Devuelve True porque 2 es igual a 2 
print(2==2.0)#Devuelve True porque 2 es igual a 2.0 aunque tenga un punto decimal python hace la conversion de entero a flotante para devolver el resultado.
#Nota: Todos los operadores relacionales nos evaluarán una condición.
#-------------------------------CONDICIONES QUE DEVUELVEN TRUE--------------------------
#Mayor que ">" Devuelve true si el de la izquierda es mayor al de la derecha
print(5>4)
#Menor que "<"Devuelve true si el de la izquierda es menor al de la derecha
print(4<5)
#Mayor o igual ">=" Devuelve true si el de la izquierda es mayor o igual que el de la derecha
print(5>=4)
print(5>=5)
#Menor o igual "<="Devuelve true si el de la izquierda es menor o igual que el de la derecha
print(4<=5)
print(5<=5)
#igual que "==" Devuelve true si el de la izquierda es igual al de la derecha
print(5==5)
print("Juan"=="Juan") #Tambien podemos evaluar cadenas
#Diferente a "!=" Devuelve true si el de la izquierda es diferente al de la derecha 
print(4!=5)
#---------------------------CONDICIONES QUE DEVUELVEN FALSE-----------------------------
#Mayor que ">" Devuelve false si el de la izquierda es mayor al de la derecha
print(4>5)
#Menor que "<"Devuelve false si el de la izquierda es menor al de la derecha
print(5<4)
#Mayor o igual ">=" Devuelve false si el de la izquierda es mayor o igual que el de la derecha
print(4>=5)
print(5>=6)
#Menor o igual "<="Devuelve false si el de la izquierda es menor o igual que el de la derecha
print(5<=4)
print(6<=5)
#igual que "==" Devuelve false si el de la izquierda es igual al de la derecha
print(5==6)
print("Juan"=="Pedro")
#Diferente a "!=" Devuelve true si el de la izquierda es diferente al de la derecha 
print(5!=5)