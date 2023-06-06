import random

r = random.randint(1, 100)
count = 0
guess = 0
while guess != r:
	guess = input('Please make a guess: ')
	count += 1
	guess = int(guess)
	if guess > r:
		print('The number is smaller')
	elif guess < r:
		print('The number is bigger')
	print('This is', count, 'guess')
print('You are correct!')
