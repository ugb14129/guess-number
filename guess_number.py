import random
r = random.randint(1 , 100)

while True:
	num = int(input('Please guess a number: '))
	if num == r:
		print('Matched')
		break
	elif num > r:
		print('Guess larger than the number')
	elif num < r:
		print('Guess less than the number')

