def get_valid_input():
    stock = input('Enter a stock: ')
    if stock == "quit":
        return "Quit"
    elif stock.isdigit() == False:
        return "Invalid No."
    else:
        return int(stock)
def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total
def calculate_tax(amount):
    tax = 0.1
    amount_tax = amount * tax 
    return amount_tax
def generate_report(total_units, failed_attempts):
    print("Total Unit Processed:", total_units ,"|", "No. of rejected entries:", failed_attempts)


inventory = 0
rejected = 0

while True:
    entry = get_valid_input()
    if entry == "Quit":
        break
    elif entry == "Invalid No.":
        print("Error")
        rejected += 1
    elif inventory + entry > 500:
        print("Units exceeded 500 units")
        break
    else:
        inventory = process_delivery(inventory, entry)
        calculate_tax(entry)

generate_report(inventory, rejected)

    
