import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


quit = False
dif_input = True
while not quit:
    while dif_input == True:
        dif = input("Choose your difficulty (Easy, Medium, Hard) ")
        dif = dif.lower()
        if (dif.lower() == 'easy'):
            range = 100
            dif_input = False
        elif (dif.lower() == 'medium'):
            range = 1000
            dif_input = False
        elif (dif.lower() == 'hard'):
            range = 10000
            dif_input = False
        else:
            print('Please choose either Easy, Medium, or Hard.')
            dif_input = True
    random_number = random.randint(1,range)
    count = 1
    number = -1
    while number != random_number:
        number = input('Please guess a number between 1 and {}: '.format (range))
        if not number.isdigit():
            print ('Please guess a number.')
        else:
            number = int(number)
            print ('Not quite, please try again!')
            if number > random_number:
                print ("Hint: that number's too high!")
            if number < random_number:
                print ("Hint: that number's too low!")
            count = count + 1
    print ('Congrats, you guessed it!!')
    print ('It only took you {} tries.'.format (count))
    play_again = input('\nWanna play again? (Yes or No) ')
    play_again = play_again.lower()
    if play_again == 'yes':
        quit = False
    else:
        quit = True
print("\n\nLet's play again sometime :)")