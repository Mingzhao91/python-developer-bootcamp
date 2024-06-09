transactions = [10.2, 31.32, 5]

transactions.append(7.82)
print(transactions)
transactions.pop()
print(transactions)

transactions.insert(1, 40.8)

print(transactions[1])
print(sum(transactions))

phone_book = {
  'alice': '223-123',
  'bob':'324-456'
}

print(phone_book['alice'])


# error
# print(min([1,2,3,4,'a','b','5']))