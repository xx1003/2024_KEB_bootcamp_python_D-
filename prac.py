# 8.11
odd = {i for i in range(10) if i % 2 != 0}
print(odd)

# 8.12
letters = (letter for letter in "Got")
for letter in letters:
    print(letter, end=' ')
print()
numbers = (number for number in range(10))
for number in numbers:
    print(number, end=' ')
print()

# 8.13
keys = ('optimist', 'pessimist', 'troll')
values = ('The glass is half full', 'The glass is halt empty', 'How did you get a glass?')
d = dict()
for key, value in zip(keys,values):
    d[key]=value
print(d)

d2 = {key:value for key, value in zip(keys,values)}
print(d2)

# 8.14
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = {title:plot for title, plot in zip(titles, plots)}
print(movies)