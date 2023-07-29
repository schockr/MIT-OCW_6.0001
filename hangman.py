# MIT OCW 6.0001
# Problem Set 2, hangman.py
# Name: Robert Schock

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char in letters_guessed:
            continue
        else:
            return False
    
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    guessed_word = secret_word
    #'_ '*len(secret_word)
    
    for char in secret_word:
        if char in letters_guessed:
            continue
        else:
            guessed_word = guessed_word.replace(char,'_ ')
    
    return guessed_word
    


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    possible_letters = string.ascii_lowercase
    for char in letters_guessed:
        if char in possible_letters:
            possible_letters = possible_letters.replace(char,'')

    return possible_letters    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    print('Welcome to the game of Hangman!')
    print('I am thinking of a word that is ',len(secret_word),'letters long.')
    
    guesses_remaining = 6 # number of guesses
    warnings = 3 # number of warnings
    letters_guessed = list() # list of letters guessed
    
    unique_letters = len(set(secret_word)) # number of unique letters in secret word
    guessed_word = get_guessed_word(secret_word,letters_guessed) # initialize guessed word
    previous_guessed_word = guessed_word # initialize previous guess
    
    while guesses_remaining>0:
        print('-----------')             
        print('You have',warnings,'warnings left.')
        print('You have',guesses_remaining,'guesses left.')
        print('Available letters:',get_available_letters(letters_guessed))
        current_guess = str.lower(input('Please guess a letter:'))
        guessed_word = get_guessed_word(secret_word,letters_guessed)
        previous_guessed_word = guessed_word
        
        # conditionals to validate user input or check if word correctly guessed
        if not str.isalpha(current_guess):
            # you lose a warning/guess due to invalid input
            # proceed to next iteration of loop and prompt reentry
            if warnings <= 0:
                guesses_remaining-=1
                print('Oops! That is not a valid letter. You have no warnings left so you lose one guess:',guessed_word)
            else:
                warnings-=1
                print('Oops! That is not a valid letter. You have',warnings,'warnings left:',guessed_word)
            continue
        elif current_guess in letters_guessed:
            if warnings <= 0:
                guesses_remaining-=1
                print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess:',warnings)
            else:
                warnings-=1
                print('Oops! You\'ve already guessed that letter. You have',warnings,'warnings left:',warnings)
            continue
        else: 
            letters_guessed.append(current_guess)
    
            if is_word_guessed(secret_word,letters_guessed):
                total_score = guesses_remaining*unique_letters
                print('---------')
                print('Congratulations, you won!')
                print('Your total score for this game is:',total_score)
                return total_score
            else:
                guessed_word = get_guessed_word(secret_word,letters_guessed)
                if guessed_word != previous_guessed_word:
                    print('Good guess:', guessed_word)
                else:
                    print('Oops! That letter is not in my word:',guessed_word)
                    if current_guess in ['a','e','i','o','u']:
                        guesses_remaining-=2
                    else:
                        guesses_remaining-=1
    
    
    if guesses_remaining <= 0 and guessed_word != secret_word:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was',secret_word)
        total_score = 0
        
    return total_score
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.strip().replace("_ ","_") # shorten to compare real word lengths
    if len(other_word)!= len(my_word):
        return False
    else:
        index = 0
        unique_letters = set(my_word) # number of unique letters in secret word
        

        for char in my_word:
            # check if letter is in other word
            # also check if other word contains multiple instances of a letter for the current index
            # since when a letter is guessed, all positions of the letter in my_word would be revealed
            if (char!='_'):
                if (other_word[index]!=char):
                    return False                    
            if (char=='_'):
                if (other_word[index] in unique_letters):
                    return False
            index+=1
            
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_word_list = list()
    for word in wordlist:
        if match_with_gaps(my_word,word):
            possible_word_list.append(word)
    
    if len(possible_word_list)>0:
        print(possible_word_list)
    else:        
        print("No matches found")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game of Hangman!')
    print('I am thinking of a word that is ',len(secret_word),'letters long.')
    
    guesses_remaining = 6 # number of guesses
    warnings = 3 # number of warnings
    letters_guessed = list() # list of letters guessed
    
    unique_letters = len(set(secret_word)) # number of unique letters in secret word
    guessed_word = get_guessed_word(secret_word,letters_guessed) # initialize guessed word
    previous_guessed_word = guessed_word # initialize previous guess
    
    while guesses_remaining>0:
        print('-----------')             
        print('You have',warnings,'warnings left.')
        print('You have',guesses_remaining,'guesses left.')
        print('Available letters:',get_available_letters(letters_guessed))
        current_guess = str.lower(input('Please guess a letter:'))
        guessed_word = get_guessed_word(secret_word,letters_guessed)
        previous_guessed_word = guessed_word
        
        # conditionals to validate user input or check if word correctly guessed
        if current_guess=='*':
            print('Possible word matches are:')
            show_possible_matches(guessed_word)
            continue
        if not str.isalpha(current_guess):
            # you lose a warning/guess due to invalid input
            # proceed to next iteration of loop and prompt reentry
            if warnings <= 0:
                guesses_remaining-=1
                print('Oops! That is not a valid letter. You have no warnings left so you lose one guess:',guessed_word)
            else:
                warnings-=1
                print('Oops! That is not a valid letter. You have',warnings,'warnings left:',guessed_word)
            continue
        elif current_guess in letters_guessed:
            if warnings <= 0:
                guesses_remaining-=1
                print('Oops! You\'ve already guessed that letter. You have no warnings left so you lose one guess:',warnings)
            else:
                warnings-=1
                print('Oops! You\'ve already guessed that letter. You have',warnings,'warnings left:',warnings)
            continue
        else: 
            letters_guessed.append(current_guess)
    
            if is_word_guessed(secret_word,letters_guessed):
                total_score = guesses_remaining*unique_letters
                print('---------')
                print('Congratulations, you won!')
                print('Your total score for this game is:',total_score)
                return total_score
            else:
                guessed_word = get_guessed_word(secret_word,letters_guessed)
                if guessed_word != previous_guessed_word:
                    print('Good guess:', guessed_word)
                else:
                    print('Oops! That letter is not in my word:',guessed_word)
                    if current_guess in ['a','e','i','o','u']:
                        guesses_remaining-=2
                    else:
                        guesses_remaining-=1
    
    
    if guesses_remaining <= 0 and guessed_word != secret_word:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was',secret_word)
        total_score = 0
        
    return total_score
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
