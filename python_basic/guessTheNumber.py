import random
secret_number = random.randint(1,20)
print("Number between 1 and 20.")

#number_of_guess = 6

for guesses_taken in range(1,7):
    print('take 6 guess')
    guess=int(input('>'))

    if guess < secret_number:
        print('too low')
    elif guess > secret_number:
        print('too large')
    else:
        break

if guess == secret_number:
    print('Good job! You got it in' + str(guesses_taken) + 'guesses!')
else:
    print('The number is %s', secret_number)