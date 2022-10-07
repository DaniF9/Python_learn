print("  ** Este programa muestra tu indice de masa corporal ** ")
peso = input("Ingrese su peso en Kg :")
estatura = input("Ingrese su estatura : ")
imc = round(float(peso)/float(estatura) ** 2.2)
print("Tu indice de masa corporal es : " , imc)

#Python proporciona una función incorporada round() que redondea al
#  número dado de dígitos y devuelve el número de punto flotante, 
# si no se proporciona ningún número de dígitos para redondear, redondea el número al entero más cercano.