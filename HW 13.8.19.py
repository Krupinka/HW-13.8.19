tickets = int(input('Enter a quantity of tickets: '))
payment = 0

for ticket in range(tickets):
    age = int(input('Enter an age: '))
    if age < 18:
        pass
    elif age >= 18 and age <= 25:
        payment += 990
    else:
        payment += 1390
    payment = payment

if tickets > 3:
    payment = payment - (payment/100 * 10)

print(f'Your bill for payment is ${payment}')



