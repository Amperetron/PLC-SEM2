def level_load(current_level):
  print("\n**********************************")
  print(f"           Level - {current_level}         ")

def next_level_load(e_health,p_health): ##enemy health and player health taken as arguments, this will do nothing rn since we dont have a loop.
  c_level = 1 
  if e_health <=0 and p_health>0:
    c_level += 1 
    level_load(c_level) ## when the condition is true it increments the level count and goes back to the level_load() to load next level.

