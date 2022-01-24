# es un tipo de dato

from calendar import month


x=(1,2,3)

print(x)

month=('january','february')

#se puede guardar directamente como  'tuple'
# y=tuple((1,2,3))

# print(y)

#se puede ver que las tuplas tienen menos operaciones que las listas
#no se pueden modificar---> es inmutable
#print(dir(x))

#x=(1) # no es una tupla, al tener un solo elemento

#x=(1,) # para hacer una tupla de un solo elemnto se le debe agregar una coma 

#Las tuplas se pueden ver unidas a diccionarios

locations={
    (35.1512,39.00574):'tokyo',
    (40.59525,39.255):'new york'
}