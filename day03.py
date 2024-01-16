# prime number
number = int(input("Input number : "))
isPrime = True  # int -> bool
i = 2
while i < number:
    if number % i == 0:
        isPrime = False  # remove +
        break
    # print(i, end=' ')
    i += 1

if isPrime:  # remove ==
    print(f'{number} is prime number')
else:
    print(f'{number} is NOT prime number!')
