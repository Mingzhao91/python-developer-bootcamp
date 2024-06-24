potions = { 
  "Invisibility Potion": ["Moonstone", "Dragon scale", "Fairy dust"], 
  "Flying Potion": ["Phoenix feather", "Troll tooth", "Mermaid scale"], 
  "Healing Potion": ["Unicorn horn", "Elf hair", "Golden apple"]
}

print('Welcome to the Magic Potion Shop!')
print('Here are the potions we offer: ')
for key, potion in enumerate(potions):
  print(potion)

user_input = input('Which potion would you like to buy ingredients for')

print(f'The ingrediens for {user_input} are:')
for item in potions[user_input]:
  print(item)


all_purchase = True
print("Let's start buying the ingredients!")
# for item in potions[user_input]:
#   is_purchase = input(f"Do you want to buy {item}? (yes/no)")
#   if is_purchase == 'yes':
#     print(f'You bought {item}')
#   else:
#     print(f"You chose to stop shopping.")
#     all_purchase = False

idx = 0
while idx < len(potions[user_input]):
  is_purchase = input(f"Do you want to buy {potions[user_input][idx]}? (yes/no)")
    
  if is_purchase == 'yes':
    print(f'You bought {item}')
  else:
    print(f"You chose to stop shopping.")
    all_purchase = False

  idx += 1

if all_purchase:
  print(f"Congratulations! You bought all the ingredients for {potions[user_input]}")
