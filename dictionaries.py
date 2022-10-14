#diccionarios agregan datos de productos o cosas de la vida real 


product = {
    "name ": "book",
    "quantity": 3 ,
    "price":4.99
}

person = {
    "first_name ": "Carlos",
    "last_name": "Fragoso"
}

print(person.keys())
print(person.items())

#del person # eliminamos todo completo 
#person.clear() # limpia todo el diccionario

#print(type(product))


#lista que contiene un diccionario
products = [
    { "name": 'book', "price": 19.00},
    {  "name":'laptop',"price": 1000}
]

print(products)