#Escribir un programa que pregunte el nombre del usuario en la consola y después 
# de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!,
#  donde <nombre> es el nombre que el usuario haya introducido.

palabra = input(" INGRESA TU NOMBRE : ")
print("! Hola",palabra,"!")

print("  !! NUEVO PROGRAMA APRENDIENDO PYTHON REALIZADO DESDE VISUAL STUDIO CODE EN WINDOWS !!")

hora = input("Ingrese el numero de horas trabajadas  : ")
precio_hora = input("Ingrese la cantidad cobra por hora : ")

paga = int(hora) * int(precio_hora)

print("Hola " , palabra , " Tu pagas total es de : " , paga , "Pesos mexicanos")

