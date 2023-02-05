value = int(input("Enter your number : ")

if value.isnumeric()
    if int(value) % 10 == 0 and int(value) < 100:
    print("Yes, the number is less than 100 and multiple of ten")
    else:
    print("No, the number not is less than 100 and multiple of ten")

else:
    print("Error, you did not enter a number")

