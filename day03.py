# prime number
number = int(input("Input number : "))
cnt = 0
i = 1
while i <= number:
    if number % i == 0:
        cnt += 1
    i += 1

if cnt == 2:
    print(f'{number} is prime number')
else:
    print(f'{number} is NOT prime number!')


# subjects = {'python' : 'kim', 'c++' : 'sung', 'datastructure' : 'kim', 'database' : 'kang'}
# print("{0[c++]} {0[datastructure]}".format(subjects))