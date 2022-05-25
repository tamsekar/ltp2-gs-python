import random
from termcolor import colored
def get_random_word():
    words = ["pizza", "cheese", "apples"]
    word = words[random.randint(0, len(words)-1)]
    return word

def show_word(word):
    for character in word:
        print(character, " ", end="")
    print("")
    
def get_guess():
    print("Enter a letter: ")
    return input()

def process_letter(letter, secret_word, blanked_word):
    result = False
    for i in range(0,len(secret_word)):
        if secret_word[i] == letter:
            result = True
            blanked_word[i] = letter
            
    return result

def print_strikes(number_of_strikes):
    for i in range(0, number_of_strikes):
        show_strike = colored("[X] ", 'red', attrs=['blink','bold'])
        print(show_strike, end="")
    print("")

def play_word_game():
    print(colored("Playing...", 'yellow', attrs=['blink']))
    strikes = 0
    max_strikes = 3
    playing = True
    
    word = get_random_word()
    blanked_word = list("_" * len(word))

    while playing:
        show_word(blanked_word)
        letter = get_guess()
        found = process_letter(letter, word, blanked_word)
        
        if not found:
            strikes += 1
            print_strikes(strikes)
        
        if strikes >= max_strikes:
            playing = False

        if not "_" in blanked_word:
            playing = False
        
    if strikes >= max_strikes:
        game_result_win = game_result_win = colored("Winner!", 'green',attrs=['blink','bold'])
        game_result_lose = colored("Loser!", 'red',attrs=['blink','bold'])
        print(game_result_lose)
    else:
        print(game_result_win)


print(colored("Game Started..",'blue',attrs=['bold']))
play_word_game()
print(colored("Game Over!",'blue',attrs=['bold']))