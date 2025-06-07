import time
import Sequence_Creation as sc
import random
import os
#the file measures the user attempt accuracy and attempt time


def level_load(current_level,current_ph):
  #Before loading a level checks if current player health is less than 0, if true then control goes back to gameloop() in main game
  if current_ph <=0:
      gameEnd()
      clear_screen() 
      return

  #Before loading a level checks if player has finishe all 5 levels, if true then control goes back to gameloop() in main game after typing "You win the game"
  if current_level > 5:
    print("\n         You win the game!         \n\n")
    clear_screen() 
    return
  
  clear_screen()  
  print("\n**********************************")
  print(f"           Level - {current_level}         \n")
  work_loop(current_ph,current_level)

def next_level_load(c_level,p_health): ##enemy health and player health taken as arguments, this will do nothing rn since we dont have a loop.
  c_level += 1 
  level_load(c_level,p_health) ## when the condition is true it increments the level count and goes back to the level_load() to load next level.


def Input_elapsed(char_list):
    print("Type the corresponding characters shown below:")

    # Print the characters of list with numbering (chatgpt made this part)
    for i, ch in enumerate(char_list, 1):
        print(f"{i}. {ch}")

    user_inputs = []
    index = 0
    total_chars = len(char_list)

    print("\nNow type each character one by one:")
    # finally have all inputs ordered and entered into the list. time starts here.
    start_time = time.time()

    while index < total_chars:
        user_input = input(f"{index + 1}: ").strip()
        if user_input:  # avoid blank inputs
            user_inputs.append(user_input)
            index += 1

    end_time = time.time()
    # time ends here and is very accurate
    elapsed_time = end_time - start_time

    # Compare the two lists for accuracy test:
    inaccuracies = sum(1 for expected, actual in zip(char_list, user_inputs) if expected != actual)
    
    return elapsed_time,inaccuracies



def damage_count(elapsed_time,innacuracies): ##Needs tweeking, contains all damage to be done wrt innaccuracies
    if innacuracies == 0:
        e_dmg = round(200/elapsed_time,3)
        p_dmg = 0
    else:
        e_dmg = round(150/elapsed_time,3)
        p_dmg = round((e_dmg * 0.2) * innacuracies,3)
    return e_dmg,p_dmg



def player_dmg_pt():  ##The random damage done by the enemy in every turn
    p_dmgpt = round(random.uniform(2,3.5),3)
    return p_dmgpt




def work_loop(player_health,current_level):
    enemy_health = 100 
    i = 1

    while player_health>0 and enemy_health>0: ##Contains all the turns involved in a level 
        print(f"Turn {i}")

        sc_list = sc.sequence_creation(current_level + 4)
        el_t,inna = Input_elapsed(sc_list)
        e_dmg,p_dmg = damage_count(el_t,inna)
        op_dmg = player_dmg_pt()               ##damge done by enemy each turn on the player
        print(f'\nEnemy did {op_dmg} damage!')
        p_dmg += op_dmg
        
        ## this does damage to enemy and player health
        enemy_health -= round(e_dmg,3)  
        player_health -= round(p_dmg,3) ##round function is used to limit decimal values in a float


        time.sleep(1)
        print(f"\nCurrent Enemy Health = {enemy_health}")
        print(f"\nCurrent Player Health = {player_health}")
        time.sleep(1)
        i=i+1
        print("\n")


    ##Enemy defeated goes to load next level
    if player_health>0 and enemy_health <=0:
        time.sleep(0.5)
        print("Enemy defeated. Well done!\n") 
        time.sleep(0.5)
        next_level_load(current_level,player_health)


    ##player defeated goes to level load for further check 
    elif player_health <= 0:
        level_load(current_level,player_health)
        

def gameEnd(): ##Ends the game if player health goes below zero (or equal) waits for some time and then shows main menu again
  time.sleep(1)
  print("        Game Over!   \n")
  time.sleep(1)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
        





