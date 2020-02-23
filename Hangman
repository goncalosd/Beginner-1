# --- HANGMAN ---
# Programmed by Gonza

import random

countries = ['australia', 'portugal', 'peru', 'mozambique', 'france', 'russia', 'argentina', 'morocco',
             'algeria', 'switzerland', 'denmark', 'mongolia', 'mexico', 'uruguay', 'spain', 'finland', 'japan']
cities = ['sydney', 'istambul', 'casablanca', 'lisbon', 'brisbane', 'newyork', 'london', 'santiago', 'arequipa',
          'montevideo', 'chicago', 'glasgow', 'berlin', 'shangai', 'toronto', 'paris', 'moscow', 'cusco', 'tokyo']
hard = ['ombudsman', 'acquaintance', 'legitimate', ]


class Class:
    word = ' '
    hangman = 6


def choice():
    print('''
Which type of word would you like?
    ''')
    game = input('''Select 1 for Countries
Select 2 for Cities
Select 3 for Hard:
    ''')

    if game == str(1):
        Class.word = random.choice(countries).upper()
    elif game == str(2):
        Class.word = random.choice(cities).upper()
    elif game == str(3):
        Class.word = random.choice(hard).upper()
    else:
        print('Please make valid selection!')
        choice()


choice()

word_list = list(Class.word)

list_hidden = []

for i in range(len(word_list)):
    list_hidden.append('-')

letters_guessed = []


def game_display():
    print('''
    ''')
    print(list_hidden)
    print('Letters guessed:')
    print(letters_guessed)
    print('Hangman: ' + str(Class.hangman) + ' tries left!')
    print('')


def letter_guess():
    game_display()
    guess = input('''
Guess a letter or word: ''').upper()
    ind_list = []

    if guess == Class.word:
        print('''You win!
        ''')

    elif guess in letters_guessed:
        print('You already guessed this letter!')
        letter_guess()

    elif guess in word_list:
        for index, i in enumerate(word_list):
            if i == guess:
                ind_list.append(index)

        for i in ind_list:
            list_hidden[i] = guess

        print('''
-> Good guess!''')

        if '-' not in list_hidden:
            print(list_hidden)
            print('''You win!
            ''')
        else:
            letter_guess()

    else:
        if len(guess) == 1:
            print('''
-> Letter not in word!''')
            Class.hangman -= 1
            if Class.hangman == 0:
                print('Hangman: ' + str(Class.hangman) + ' tries left!')
                print('Word was: {}'.format(Class.word))
                print('You lost!')
            else:
                letters_guessed.append(guess)
                letter_guess()
        else:
            print('''
-> Wrong word!''')
            Class.hangman -= 1
            if Class.hangman == 0:
                print('Hangman: ' + str(Class.hangman) + ' tries left!')
                print('Word was: {}'.format(Class.word))
                print('You lost!')
            else:
                letter_guess()


letter_guess()
