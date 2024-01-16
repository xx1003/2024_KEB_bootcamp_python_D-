# 연습문제 6.1
numbers = [3, 2, 1, 0]
for number in numbers:
    print(number, end = ' ')

print()

for number in range(3, -1, -1):
    print(number, end = ' ')

print()


# 연습문제 6.2
guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break

    number += 1


# 연습문제 6.3
guess_me = 5

for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
