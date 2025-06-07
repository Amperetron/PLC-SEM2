import random 

def sequence_creation(n):
  seq = []
  for i in range (n):

    l_choice = random.randint(0,1)  #To choose one between uppercase and lowercase for each charcter

    ch_choice = random.randint(65,90) #To choose an ascii value of uppercase letter for each letter in the sequence 

    match l_choice:
      case 0: #For upppercase
        char = chr(ch_choice)
        seq.append(char) #We  simply concatenate to seq by converting to ascii

      case 1: #For lowercase
        char = chr(ch_choice + 32)
        seq.append(char) #if choice is lowercase, we first convert uppercase ascii to lowercase and concatenate

  return seq

 