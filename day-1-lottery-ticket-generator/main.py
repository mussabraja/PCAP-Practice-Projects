import random
def generate_tickets(ticket_count,max_number):
    list_rand = []
    while len(list_rand) < ticket_count:
        x = random.randint(0, max_number - 1)
        if x not in list_rand:
            list_rand.append(x)
    aa = (random.choice(list_rand))
    return (list_rand,aa)




print(generate_tickets(5,10))
