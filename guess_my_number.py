print('Please think of a number between 0 and 100!')
print('Is your secret number 50?')
ask = input('Enter '"h"' to indicate the guess is too high. Enter '"l"' to indicate the guess is too low. Enter '"c"' to indicate I guessed correctly. ')

low = 0
high = 100
guess = (high + low)//2
while 'c' != ask:
    if 'l' == ask:
        low = guess
        guess = abs(low + high) // 2
    elif 'h' == ask:
        high = guess
        guess = abs(low + high) // 2
    else:
        print('Sorry, I did not understand your input.')
    print('Is your secret number', guess,'?')
    ask = input('Enter '"h"' to indicate the guess is too high. Enter '"l"' to indicate the guess is too low. Enter '"c"' to indicate I guessed correctly. ')

print('Game over. Your secret number was:', guess)

