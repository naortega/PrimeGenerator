number = 3
primes = [2]

while 1:
    for prime in primes:
        if not number % prime: #In python 0, empty collections and None evaluates to 0
            break
    else: #This is the loop's else statement. It executes if the loop runned entirely
        primes.append(number)
        print("Found prime number:", number)
    number += 1