import decimal #Decimal doesn't come standard with Python

customer_type = input("enter R for retail or W for wholesale: ")
customer_type = customer_type.lower() # para que equivalga a si mismo pero en minuscula por si acaso alguien lo pone en minus
invoice_total = float(input("enter invoice total: "))
dis = 0.0 # The discount to be determined

if customer_type == "R":
    if invoice_total >= 100.00 and invoice_total < 250:
        dis = 0.1
    elif invoice_total >= 250:
        dis = 0.2
elif customer_type == "W":
    if invoice_total < 500.00:
        dis = 0.4
    elif invoice_total >= 500.00:
        dis = 0.5
else:
    print("Code is not valid.")

print(f"Discount determined is {dis}")