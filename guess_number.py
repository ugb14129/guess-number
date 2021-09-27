import random
r = random.randint(1 , 100)
count = 0
while True:
	count = count + 1
	num = int(input('Please guess a number: '))
	if num == r:
		print('Matched')
		print('This is your' , count , 'time')
		break
	elif num > r:
		print('Guess larger than the number')
	elif num < r:
		print('Guess less than the number')
	print('This is your' , count , 'time')

