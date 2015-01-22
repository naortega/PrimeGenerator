x = 1

while True:
	isPrime = False
	for i in range(2, x / 2 + 1):
		if x % i == 0:
			isPrime = True
			break
	if isPrime is False: print x, "is prime."
	x += 1
