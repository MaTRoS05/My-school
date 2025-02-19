import random

def get_numbers_ticket(min, max, quantity):
    random_numbers = random.sample(range(min, max + 1), quantity)
    return sorted(random_numbers)

min_value = 1
max_value = 1000
quantity_value = 10

ticket_numbers = get_numbers_ticket(min_value, max_value, quantity_value)

print("Generated ticket numbers:", ticket_numbers)
