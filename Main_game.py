import time

p_max_health = 100.0
e_max_health = 100.0

def mainMenuDisplay():
  mainf = open("Main_Menu.txt",'r')
  mainf_c = mainf.read()
  print(mainf_c)
  mainf.close()
  mainMenuChoice()

def mainMenuChoice():
  ch = input("Enter a choice: ")
  if ch == '1':
    gameLoop(p_max_health)
  elif ch == '2':
    quit()
  else:
    print("Invalid Input \n")
    mainMenuChoice()

def gameLoop(p_he):
   ## The game loop will be there here.

   ##For debugging purpose
    while p_he > 0:
      dmg = int(input("Enter damage: "))
      p_he -= dmg
      print(f"Player health {p_he}")
    gameEnd(p_he)
    ## Just to check if other functions are working

def gameEnd(p_health):
  if p_health <= 0:
    time.sleep(1)
    print("\n\n         Game Over!   \n\n")
    time.sleep(1)
    mainMenuDisplay()



mainMenuDisplay()
