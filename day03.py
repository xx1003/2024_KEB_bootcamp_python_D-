import random

while True:
    print("<Guess Number Game Start>")
    guess_num = random.randint(1, 11)
    for i in range(10):
        number = int(input("Guess number!(1 ~ 10) : "))
        if number < guess_num:
            print("Too low!")
        elif number == guess_num:
            print("Found it!")
            break
        else:
            print("Too high!")
    else:
        print("You failed ㅠㅠ")

    menu = input("1) Try again  2) Quit game : ")
    if menu == '1':
        continue
    elif menu == '2':
        break





