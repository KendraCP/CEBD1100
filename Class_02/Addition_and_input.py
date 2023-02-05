first_number = input("Enter the first number : ")
second_number = input("Enter the second number : ")

our_sum = first_number + second_number

print(our_sum) # eso imprimiria 23, porque si el primer number oes 2 y el tercero es 3 caundo haces una suma de un string in pyhton the result of an adtion of two strings is a concetenation. we do ahce a trick, is converting. in our example is I was to add 2+3 not string, int, is additon, is 5. There are some fontiones inside of python, the first is int, int means take a string and convert it float take a string converted into a float, take a int and convert to a string, that's str

our_sum_corrected = int(first_number) + int(second_number)

print(our_sum_corrected)
