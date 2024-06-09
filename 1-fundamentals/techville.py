def move_forward():
  print("moving forward")

def turn(direction):
  print(f"turning {direction}")

def start_engine():
  print("starting engine")

def stop_engine():
  print("stopping engine")

def follow_roundabout(exit_number):
  print(f"taking exit number {exit_number} from the roundabout")


start_engine()
destination = input('Where do you want to go?')

if destination == 'library':
  move_forward()
  turn('left')
  print('arrived')
elif destination == 'tech park':
  move_forward()
  turn('right')
  print('arrived')
elif destination == 'hospital':
  move_forward()
  follow_roundabout(1)
  print('arrived')
elif destination == 'mall':
  move_forward()
  follow_roundabout(2)
  move_forward()
  turn('right')
  print('arrived')
elif destination in ['university', 'stadium']:
  follow_roundabout(4)
  if destination == 'university':
    turn('left')
    print('arrived')
  if destination == 'stadium':
    turn('right')
    print('arrival')

stop_engine()
