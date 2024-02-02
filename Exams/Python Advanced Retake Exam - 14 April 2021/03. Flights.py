def flights(*args):
    final = {}
    for i in range(0, len(args)-1, 2):
        destination = args[i]
        passenger = args[i+1]
        if destination == 'Finish':
            break
        else:
            if destination not in final:
                final[destination] = 0
            final[destination] += passenger

    return final


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
