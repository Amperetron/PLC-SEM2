def level_load(current_level):
  print("\n**********************************")
  print(f"           Level - {current_level}         ")

def next_level_load(e_health,p_health):
  c_level = 1 
  if e_health <=0 and p_health>0:
    c_level += 1 
    level_load(c_level)

