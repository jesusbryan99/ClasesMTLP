while True:
    numero1= float(input("Ingresa el primer numero"))
    numero2= float(input("Ingresa el Segundo numero"))
    operacion= input("Ingresa la operacion que deseas realizar + - / *")
   
    if operacion == "+":
        resultado = numero1+numero2
        print("el resultado de la suma es:",resultado)
    elif operacion == "-":
        resultado = numero1-numero2
        print("el resultado de la resta es:",resultado)
    elif operacion == "/":
        resultado = numero1/numero2
        print("el resultado de la division es:",resultado)
    elif operacion == "*":
        resultado = numero1*numero2
        print("el resultado de la multiplicacion es:",resultado)
    else:
        print("Operacion no valida.")
        numero1= float(input("Ingresa el primer numero"))
        numero2= float(input("Ingresa el Segundo numero"))
        operacion= input("Ingresa la operacion que deseas realizar + - / *")
        
    pregunta = input("¿Deseas realizar otra operacion? (si/no)")
    if pregunta == "si":
        print("Continuemos")
        continue
    elif pregunta == "no":
        print("Hasta luego")  
        break
    else:
        print("Operacion no valida")