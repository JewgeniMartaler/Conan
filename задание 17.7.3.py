per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money  = int(input("введите сумму вклада:"))
from decimal import Decimal

deposit = []
deposit.append(per_cent['ТКБ'] * money / 100)
deposit.append(per_cent['СКБ'] * money / 100)
deposit.append(per_cent['ВТБ'] * money / 100)
deposit.append(per_cent['СБЕР'] * money / 100)

print()
print(deposit)

max_deposit = max(per_cent.values())
print()
print("Максимальная сумма, которую вы можете заработать:", max_deposit * money / 100)