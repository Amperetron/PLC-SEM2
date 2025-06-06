import time
#the file measures the user attempt accuracy and attempt time

'''
Note to pro jr dev Amith Aravind Pai
this program requrires the following while calling:
1. a list form your side as the input prompt

this program gives out the following:
1. the ordered output of elements in your provided list (seqence_creation.py)
2. final output of time elapsed and the accuracy 

this program takes the following input in run time:
1. while loop to do the following: index+1 of list + <user input> 
'''


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
# the following lines are just for debugging (made by chatgpt) and can be later moded for return values as requred !!
    print(f"Time Elapsed: {elapsed_time:.2f} seconds")
    print(f"Inaccuracies: {inaccuracies} out of {total_chars}")
# test out function totally:
print(Input_elapsed(['A','d','I','t','Y','a']))

'''
Type the corresponding characters shown below:
1. A
2. d
3. I
4. t
5. Y
6. a

Now type each character one by one:
1: a
2: d 
3: i
4: t
5: Y
6: a

--- Result ---
Time Elapsed: 18.97 seconds
Inaccuracies: 2 out of 6
'''