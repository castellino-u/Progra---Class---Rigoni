def addresses(shopping):
    addresses=[]
    clients=[]
    for n in range(len(shopping)):
        addresses.append((shopping[n])[-1])
        clients.append((shopping[n])[0])
    addresses_without_repeating=[]
    clients_without_repeating=[]
    for a in range(len(addresses)):
        counter=0
        for b in range(len(addresses_without_repeating)):
            if addresses[a]==addresses_without_repeating[b]:
                counter+=1
        if counter==0:
            addresses_without_repeating.append(addresses[a])
    return addresses_without_repeating

def clients(shopping):
    clients=[] 
    for n in range(len(shopping)):
        clients.append((shopping[n])[0])
    clients_without_repeating=[]
    for a in range(len(clients)):
        counter=0
        for b in range(len(clients_without_repeating)):
            if clients[a]==clients_without_repeating[b]:
                counter+=1
        if counter==0:
            clients_without_repeating.append(clients[a])
    return clients_without_repeating