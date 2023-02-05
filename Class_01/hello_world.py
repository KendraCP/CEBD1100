print("TESTING 123")
a=1000
print(type(a))
a=1000.20


print(type(a))
TAX_RATE = 0.15
person_a_meal = 45.00
person_b_meal = 55.44

print(person_a_meal * (1 + TAX_RATE)) # Solo tienes que cambiar el tax rate en un lugar y no uno por uno si cambia el tax rate. Si no es un magic number, un numero que no sabemso de donde ha salido
print(person_b_meal * 1.15)

amount_of_tax = person_a_meal * TAX_RATE # Por este tipo de cosas ponemos 0.15 en el tax rate y no directamente el 1.15
# se pueden poner parentesis, por ejemplo el de la persona a, sin el parentesis no funcionaria matematicamente, porque las multiplicaciones van primero
