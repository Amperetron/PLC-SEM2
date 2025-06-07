import BackendEngine as BE

p_max_health = 100.0 #maximum player health at the beginning of the game  

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
  first_level = 1

  #in the beginning of the game, we initalize current health to max health 
  current_ph = p_he
  BE.level_load(first_level,current_ph)
  mainMenuDisplay()

mainMenuDisplay()