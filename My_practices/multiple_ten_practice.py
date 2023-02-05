nb = input("Choose a number : ")

if nb.isnumeric():
    if float(nb) % 10 == 0 :
        if float(nb) < 100 :
            print("Yes, the number is a multiple of 10 and less than 100")
        else:
            print("The number is a multiple of ten an more than 100")
    elif float(nb) % 10 != 0 :
        if float(nb) < 100:
            print("No, the number is not a multiple of 10 and is less than 100")
        else:
            print("The number is not a multiple of ten an more than 100")
else:
    print("Please, enter a valid number")

print("Program finishing")

