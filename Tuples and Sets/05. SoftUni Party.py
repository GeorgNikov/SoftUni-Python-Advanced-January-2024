n = int(input())

reservations = set()

for _ in range(n):
    reservations_ticket = input()
    reservations.add(reservations_ticket)

reservation_ticket = input()

while reservation_ticket != 'END':
    if len(reservation_ticket) == 8:
        if reservation_ticket in reservations:
            reservations.remove(reservation_ticket)
            continue

    reservation_ticket = input()

print(f'{len(reservations)}')
sorted_reservation = sorted(reservations)
print(*sorted_reservation, sep='\n')
