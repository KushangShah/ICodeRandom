# defining a game variable with single input
def vow_cons(string):

    # creating parameter for vowels
    vowels = "AEIOU"

    # initialising 0 to vow and cons in begining
    vow = 0
    cons = 0

    # getting lenght og string to get substring of string
    length = len(string)

    # using for loop to iterate over string
    for i in range(length):

        # checking if string is in vowel or not
        if string[i] in vowels:
            vow += length - i
        else:
            cons += length - i
    # checking if vow is greater then cons or not
    if vow > cons:
        winner = "Player 1"
        score = vow
    
    elif cons > vow:
        winner = "Player 2"
        score = cons
    # If both have same score than print Draw
    else:
        winner = "Draw"
        score = ''
    
    # Printing the output
    print(f"{winner} {score}")

# intialiaing init function
if __name__ =='__main__':
    string = input()
    vow_cons(string)
    