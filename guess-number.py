import random

r = random.randint(1, 100)
guess = 0
while guess != r:
	guess = input('Please make a guess: ')
	guess = int(guess)
	if guess > r:
		print('The number is smaller')
	elif guess < r:
		print('The number is bigger')
print('You are correct!')
