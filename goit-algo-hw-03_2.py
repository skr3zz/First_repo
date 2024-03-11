import random

def get_numbers_ticket(min,max,quantity):
    if min < 1 or max > 1000 or min >= max or quantity < 1 or quantity > (max - min + 1):
        return []
    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min, max))
    num_list = sorted(list(numbers_set))
    return num_list
print(get_numbers_ticket(1, 36, 5))