def dollarizer(word):
  return word.replace('s', '$')

def eurizer(word):
  return word.replace('e', '€')

def replacer(word, char1, char2):
  return word.replace(char1, char2)

def wonky_text(word):
  return replacer(dollarizer(eurizer(word)), 'i', '£') 

def celsius_to_fahrenheit(celsius):
  return celsius * 9 / 5 + 32

def age_in_days(age):
  return age * 365

def simple_interest(amount, rate, year):
  return amount * rate * year

def plan_finances(amount, rate, year, descired_amount):
  return descired_amount <= simple_interest(amount, rate, year)

print(dollarizer('esfdas'))
print(eurizer('asesfe'))
print(replacer('hello', 'l', 'k'))
print(wonky_text('hello world, i\'m human and i don\'t have apples'))
print(celsius_to_fahrenheit(95))
print(age_in_days(100))
print(simple_interest(100, 0.1, 100))
print(plan_finances(100, 0.1, 100, 100))

