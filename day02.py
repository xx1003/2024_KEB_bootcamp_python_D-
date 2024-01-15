first_number = int(input('Input first number : '))
second_number = int(input('Input second number : '))

# divmod(first, second) => (몫, 값) tuple
print(f'몫은 {divmod(first_number,second_number)[0]}, 나머지는 {divmod(first_number, second_number)[1]}')

# quotient = first_number // second_number
# remainder = first_number % second_number
# print(f'몫은 {quotient}, 나머지는 {remainder}')