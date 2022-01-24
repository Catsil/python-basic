#hay 3 tipos de modulos, el que se crea uno mismo, el que se descarga de internet o el python

#modulos preconstruidos que da python

# import datetime
# from datetime import timedelta, date # otra manera de importarlo y traerlo directamente
# import fmath #este modulo lo creamos a nuestra necesidad 

# print(datetime.date.today())

# print(datetime.timedelta(minutes=100))

# print(date.today())

# fmath.add(1,2) #se llama  el modulo que hemos creado, previamente haberlo importado

from colorama import Fore, Style, init
init(convert=True)
print(Fore.BLUE +"Hello world")
