first = "Brendan"
last = "Wood"

# Formatting

print("{} {}".format(first, last))

print("first name is {} and last name is {}".format(first, last))

print(f"first name is {first} and last name is {last}")

print("first name is {1} and last name is {0}".format(first, last))


# place holder {} means we want to put some kind of value there

# si pones una f minuscula al principio y lo que quieres dentro de los place holders tambien funciona, es un shortcut

print("{:04d}".format(42))

print("price is $ {}".format(1.7)) # pero siempre dos digitos par el dinero

print ("price is $ {:8.2f}".format(1.7)) # 8 is the total space of the entire value. If I were to remmove the 8, implies that there is no fix value

#best way, sin nada delante del decimal, se aplasta lo de delante par que no quede separado por lo del numero de lugares

print("price is $ {:.2f}".format(1.7))
