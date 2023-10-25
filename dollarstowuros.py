("print  Dollars-to-Euros ") 
("print the-purpose-of-the program and version is to convert the dollars to euros") 
("print owen-dixon-programmer ") 

while True:
    choice = input("Would you like to convert dollars to euros? (yes/no): ")
    if choice.lower() == "no":
        break
    amount = float(input("Enter dollar amount to be converted: "))
    euro = amount * 0.94540
    print("The converted euro amount is:", euro)