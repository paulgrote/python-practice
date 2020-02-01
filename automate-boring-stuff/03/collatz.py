def collatz(number):
	if number % 2 == 0:
		print(number // 2)
		return number //2
	elif number % 2 == 1:
		print(3 * number + 1)
		return 3 * number + 1

try:
	userNumber = int(input('Enter an integer: '))
	while userNumber != 1:
		userNumber = collatz(userNumber)
except:
	print('You did not enter an integer. Do better next time.')
