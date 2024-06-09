sentence1 = input("Enter a sentence:")
print(sentence.upper())

paragraph = input("Enter a paragraph: ")
print(len(paragraph.split(' ')))

sentence2 = input("Enter a sentence")
print(sentence2.isdigit())

sentence3 = input("Enter a sentence")
print(sentence3.replace('a', 'o'))

full_name = input("Enter your fullname")
words = full_name.split(' ')
initials = ''
for word in words:
  print(word)
  initials += word[:1]
print(initials)

sentence4 = input("Enter a sentence")
print(len(sentence4))



def cooking_end_time(start_time, duration):
  end_time = (start_time + duration) % 24
  return end_time




def move_forward():
  print("moving forward")

def turn(direction):
  print(f"turning {direction}")

def start_engine():
  print('start engine')

def stop_engine():
  print('stopping engine')

destination = input('where do you want to go?')

start_engine()
move_forward()

if destination == 'school':
  turn('right')
  print('we arrived at school!')
elif destination == 'grocery store':
  turn('left')
  print('we arrived at grocery store!')







