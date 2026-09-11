inventory = 0
rejected = 0
while True:
    stock = input("Enter a stock: ")
    if stock == "quit":
        break
    elif stock.isdigit() == False:
        print("Error")
        rejected += 1
    elif inventory + int(stock) > 500:
        break
    else:
        inventory += int(stock)
print("Total Unit Processed:", inventory, "No. of rejected entries:", rejected)
    
