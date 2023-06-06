import random

while True:
	start = input('Please input the start of random number: ')
	start = int(start)
	end = input('Please input the end of random number: ')
	end = int(end)
	if start <= end:
		break
	else:
		print('start should be smaller or equal to end')
r = random.randint(start, end)
count = 0
guess = 0
while guess != r:
	guess = input('Please make a guess: ')
	count += 1
	guess = int(guess)
	if guess <= end and guess >= start:
		if guess > r:
			print('The number is smaller')
		elif guess < r:
			print('The number is bigger')
	else:
		print('The number should within', start, "to", end)
	print('This is', count, 'guess')
print('You are correct!')
