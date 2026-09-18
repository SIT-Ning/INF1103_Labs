def get_valid_input():
    stock = input('Enter a stock: ')
    if stock == "quit":
        return "Quit"
    elif stock.isdigit() == False:
        return "Invalid No."
    else:
        return True
def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total
def calculate_tax(amount):
    amount_tax = amount * 0.1
    return amount_tax
def generate_report(total_units, failed_attempts):
    print("Total Unit Processed:", total_units ,"|", "No. of rejected entries:", failed_attempts)


inventory = 0
rejected = 0

get_valid_input()