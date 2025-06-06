import time

p_max_health = 100.0 #maximum player health at the beginning of the game 
e_max_health = 100.0 #this initialization for the time being  

def mainMenuDisplay():
  mainf = open("Main_Menu.txt",'r')
  mainf_c = mainf.read()
  print(mainf_c)
  mainf.close()
  mainMenuChoice()

def mainMenuChoice():
  ch = input("Enter a choice: ") ## made this choice menu only to play and exit, tutorial can also be added
  if ch == '1':
    gameLoop(p_max_health)
  elif ch == '2':
    quit()
  else:
    print("Invalid Input \n")
    mainMenuChoice()    ##Repeatedly takes input if choice is invalid 

def gameLoop(p_he):
   ## The game loop will be there here.

   ##For debugging purpose
    while p_he > 0:
      dmg = int(input("Enter damage: "))
      p_he -= dmg
      print(f"Player health {p_he}")
    gameEnd(p_he)
    ## Just to check if other functions are working

def gameEnd(p_health): ##Ends the game if player health goes below zero (or equal) waits for some time and then shows main menu again
  if p_health <= 0:
    time.sleep(1)
    print("\n         Game Over!   \n")
    time.sleep(1)
    mainMenuDisplay()



mainMenuDisplay()
