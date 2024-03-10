import random
def get_numbers_ticket(min,max,quantite):
    return {"min":min,"max":max,"quantite":quantite}
l = list(range(1, 36))
print(random.sample(l, k=5))