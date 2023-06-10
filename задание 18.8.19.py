price_all = 0
while True:
    try:
        ticket_number = input("введите количество билетов")
        ticket_number = int(ticket_number)
        if type(ticket_number) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket_number):
    i += 1
    while True:
        try:
            age_for_ticket = input(f'сколько Вам лет? №{i} ')
            age_for_ticket = int(age_for_ticket)
            if age_for_ticket < 18:
                print('билет бесплатный')
            elif 25 > age_for_ticket >= 18:
                price_all += 990
                print('стоимость билета: 990 руб.')
            else:
                price_all += 1390
                print('стоимость билета: 1390 руб.')
            if type(age_for_ticket) == int:
                break
        except ValueError:
            print('Введите целое число')
if ticket_number > 3:
    price_all = price_all - ((price_all / 100) * 10)
    print(f'сумма к оплате {price_all} руб. со скидкой 10% от полной суммы')
else:
    print(f'сумма к оплате {price_all} руб.')