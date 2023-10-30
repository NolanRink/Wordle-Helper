

# make a list of all possible words
def get_all_words(file):
    valid_words = []
    try:
        with open(file) as f:
            for words in f:
                valid_words.append(words.strip())
            return valid_words
    except FileNotFoundError:
        print('File not Found\nExiting program')
        return None
    
#get user input for a wordle guess
def get_guess(word_list):
    while(True):
        try:
            guess = str(input("Enter your guess: "))
            if len(guess) != 5 or not guess.isalpha() or guess not in word_list:
                raise ValueError
            return guess
        except ValueError:
            print("The guess must be a valid 5 letter word")
            continue

#get user input for feeedback from their guess
def get_feedback(word, feedback):
    print('Please provide the feedback (green = g, yellow = y, gray = x) e.g \'xxygx\'')
    valid_letters = 'gyx'
    while(True):
        try:
            feedback = str(input(f"Enter the feedback for {word}: "))
            if len(feedback) != 5: raise ValueError
            for letter in feedback:
                if letter not in valid_letters:
                    raise ValueError
            break
        except ValueError:
            print('Invalid input, enter a 5 letter word containing only gyx')
            continue
    return feedback

#Use the users guess and feedback to elimnate all words that no longer work
def update_words(word_list, guess, feedback):
    invalid_words = []
    letters = []
    # print(len(word_list))
    # print(word_list)
    for i in range(5):
        for word in word_list:
            
            if feedback[i] == 'g':
                if word[i] != guess[i]:
                    invalid_words.append(word)
                    if guess[i] not in letters: letters.append(guess[i])
            
            elif feedback[i] == 'y':
                if guess[i] not in word:
                    invalid_words.append(word)
                elif guess[i] == word[i]:
                    invalid_words.append(word)
                if guess[i] not in letters: letters.append(guess[i])
            
            elif feedback[i] == 'x':
                if guess[i] in word:
                    if guess[i] not in letters:
                        invalid_words.append(word)
                    elif word[i] == guess[i]:
                        invalid_words.append(word)

        
        for words in invalid_words:
            if words in word_list:
                word_list.remove(words)

    return word_list

#print a list of words wwith 10 per a line
def print_words(words):
    i = 0
    print(f"{len(words)} Possible Words:")
    for word in words:
        print(word,end =' ')
        i+=1
        if i == 10:
            print('')
            i=0
    print('')


def main():
    guess = ''
    feedback = ''
    all_valid_words = []
    all_valid_answers = []
    guess_list = []

    print("Welcome to the Wordle solver")

    all_valid_words = get_all_words('valid-wordle-words.txt')
    if all_valid_words == None: return

    #all_valid_answers = get_all_words('answers-list.txt')

    guess_list = get_all_words('answers-list.txt')#all_valid_answers.copy()

    while(True):
        guess = get_guess(all_valid_words)
        feedback = get_feedback(guess, feedback)

        guess_list = update_words(guess_list, guess, feedback)
        if not guess_list:
            print("No words match these constraints")
            return
        
        print_words(guess_list)

        again = str(input("Enter \'a\' to make another guess\n or anything other than a to quit: "))
        if again != 'a':
            break

main()
