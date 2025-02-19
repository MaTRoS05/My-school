import random

def get_numbers_ticket(min_value, max_value, quantity):
    if not (1 <= min_value <= max_value <= 1000) or quantity > (max_value - min_value + 1):
        print("Invalid input: quantity cannot be greater than the available range.")
        return []

    return sorted(random.sample(range(min_value, max_value + 1), quantity))

min_value = 1
max_value = 1000
quantity_value = 10 

ticket_numbers = get_numbers_ticket(min_value, max_value, quantity_value)
print("Generated ticket numbers:", ticket_numbers)