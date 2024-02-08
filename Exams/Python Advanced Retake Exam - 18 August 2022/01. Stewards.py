def rotate(ticket):
    result = ticket.copy()
    result[0], result[-1] = result[-1], result[0]

    return result


from collections import deque

seats = [x for x in input().split(', ')]
ticket_one = deque([int(x) for x in input().split(', ')])
ticket_two = list([int(x) for x in input().split(', ')])

seat_match = []
rotation = 0

while rotation < 10 and len(seat_match) < 3:
    current_ticket_one, current_ticket_two = ticket_one.popleft(), ticket_two.pop()
    ticket = current_ticket_one + current_ticket_two
    seat_one = str(current_ticket_one) + chr(ticket)
    seat_two = str(current_ticket_two) + chr(ticket)

    if seat_one in seats or seat_two in seats:
        if seat_one in seats and seat_one not in seat_match:
            seat_match.append(seat_one)

        if seat_two in seats and seat_two not in seat_match:
            seat_match.append(seat_two)

    else:
        ticket_one.append(current_ticket_one)
        ticket_two.insert(0, current_ticket_two)

    rotation += 1

print(f"Seat matches: {', '.join([str(x) for x in seat_match])}")
print(f"Rotations count: {rotation}")
