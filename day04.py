numbers = input("Input first second number : ").split()  # 두 수 입력 못 받으면 에러?,  간소화 가능
n1 = int(numbers[0])
n2 = int(numbers[1])

if n1 > n2:
    n1, n2 = n2, n1
for number in range(n1, n2 + 1):
    isPrime = True

    if number < 2:
            continue
    else:
        i = 2
        while i*i <= number:  # 반복 횟수 줄임
            if number % i == 0:
                isPrime = False
                break
            i += 1
            # print(i, end = ' ')  # loop count
        if isPrime:
            print(number, end=' ')
print()
