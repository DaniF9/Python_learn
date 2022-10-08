print("Realizamos la suma de dos numeros con el operador : + ")
a = 10
b = 5
c = a + b 
print("El valor de la suma es ", c)
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

print("Realizamos el modulo con el operador : % ")
a = 10
b = 3
c = 10%3
print("El resultado del modulo es : " , c) #recordamos que el modulo es el residuo o resto de una division
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

print("Ralizamos una diviosn entera con el operador : //")#recordando que una division entera nos da como resultado un numero entero
a = 9
b = 2
c = 9//2
print("El resultadora de la division entera es : " , c)

print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print(" Realizamos la potencia de un numero con el operador : **")
a = 3
b = 3
c = 3**3
print("El resultado de la potencia es : " , c)
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
print("Haremos un If pidiendo al usuario los numeros")
numero1 = int(input("Ingrese el primer numero : "))
numero2 = int(input("Ingrese el segundo numero : "))

if numero1>numero2:
  print('El primer número es mayor.')
elif numero1<numero2:
  print('El primer número es menor.')
else:
  print('Ingrese algo logico.')

print(type(numero1))
print(type(numero2))

'''problema que me encontre al hacer este if al inicio no declaraba las variables como enteras por lo cual las dejaba como string
entonces al momento de hacer el if se invertia la comparacion ya que los leia de tipo string y no de tipo entero
alo cual la solucion fue al pedir el numero ya declarar como tipo entero  numero1 = int(input("ingrese el numero 1"))'''
