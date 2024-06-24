transactions_aed = [23.45, 67.89, 12.34, 78.90, 54.21]

transactions_usd = []

for item in transactions_aed:
  item_usd = item * 0.27
  transactions_usd.append(item_usd)

print(transactions_usd)