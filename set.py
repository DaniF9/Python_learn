#se usan para definir una coleccion que no tienen un indice 

colors = {'green','blue','red','yellow'}
print(type(colors))

print('red' in colors)

colors.add('violet')
print(colors)

colors.remove('red')
print(colors)

del colors
#colors.clear()
print(colors)