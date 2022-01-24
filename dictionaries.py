#es un tipo de dato que permite definir a partir de claves y valores

car={
"name":"book",
"quantity":3,
"price":4.99
}

person={
    "first_name":"ryan",
    "last_name":"ray"
}

print(type(person))

print(person.items())

#tambien se pueden definir a partir de una lista

products=[
    {"name":"book", "price":10.99},
    {"name":"laptop", "price":10.99}
]

print(products)