# name = input("What is your name")
# print(f"Hello {name}")

numbers = [1,2,4,5]
printable_numbers = repr(numbers)
print(type(printable_numbers))
print(printable_numbers)


numbers = [1,45,31,12,60, 8]
for number in numbers:
   if number % 8 == 0:
       # reject the list
       print('The numbers are unacceptable')
       break
else:
   print('All those numbers are fine')


name1 = input('Enter your name: ')
name1_capitalized = name1.capitalize()
name2 = input('Enter your name: ')
name2_capitalized = name2.capitalize()
name3 = input('Enter your name: ')
name3_capitalized = name3.capitalize()


print(f"The names are: {name1_capitalized}, {name2_capitalized} and {name3_capitalized}")


