# squares = list()
# for i in range(1,6):
#     squares.append(i*i)
# print(squares)

# list comprehension
# squares = [i*i for i in range(1, 6, 1)]
# print(squares)

even = [i*i for i in range(1, 6, 1) if i % 2 == 0]
print(even)