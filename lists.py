# demo_list=[1,'hello',1.32, True, [1,2,3]]
#colors=['red','blue', 'pink']

# #constructor
# numbers_list=list((1,2,3))
# print(numbers_list)
n=int(input('insert number'))
print(n)

r=list(range(0,n))
print(r)

for element in r:
    element=element*element
    print(element)

#print(r**2)

# print(type(colors))
# #print(dir(colors)) #con este comando se obtiene informacion de lo que se puede hacer con la variable colors
# print(colors[0])
# print('green' in colors)

# colors[1]='yellow'

# #print(dir(colors))

# colors.append('violet','black')


#colors.extend(['white','black'])

# colors.insert(3, 'violet')

# colors.insert(len(colors), 'violet')
# print(colors)   

#colors.pop()  #elimina el ultimo elemento, a menos que se indique la posicion

#colors.remove('red')
#colors.clear() #borra todos los elementos de la lista

#colors.sort() #ordena alfabeticamente

#colors.sort(reverse=True) #ordena de forma inversa al alfabeto

#print(colors.index('blue'))  #indica el numero del indice del elemento requerido


# print(colors.count('red'))

# print(colors)