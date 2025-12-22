"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

def bonus_for_special_total():
    """bonus rule for player whos rolls total 2 or 7.
    player win or lose recieves a 10 mon bonus"""
    if dice1 ==1 and dice2 ==1:#check for outcome of 1 and 1 dice roll
        return "snake eyes you win a 10 mon bonus"
    elif dice1 and dice2 == 7:## check for outcome of 7 diceroll
        return "lucky seven you win a 10 mon bonus"

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.    SPECIAL NOTICE: if the player recieves a dice roll total of  a 2(1-1)  or a 7 a 10 Mon bonus
''')
    #UPDATED:added notice to introduction concerning rolls with total of 2 or 7
purse = 5000
bonus_purse: int = purse + 10

while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:

    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    dice_total = dice1 + dice2

    if dice_total == 2 or dice_total == 7:# check for special values
     print('You won a bonus of 10 mon!')#inform user of bonus
     




    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')

        purse = purse + pot  # Add the pot from player's purse.
        print('The house collects a', pot // 12, 'mon fee.')
        purse = purse - (pot // 12)  # The house fee is 12%. #UPDATED   house percentage to 12% from 10%
    else:
        purse = purse - pot  # Subtract the pot from player's purse.
        print('You lost!')

            # Check if the player has run out of money:
        if purse == 0:
         print('You have run out of money!')
         print('Thanks for playing!')
        sys.exit()
