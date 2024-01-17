# 8.1
e2f = {"dog" : "chien", "cat" : "chat", "walrus" : "morse"}
e2f_2 = dict(dog="chien", cat="chat", walrus="morse")
print(e2f, e2f_2)
print()

# 8.2
print(e2f["walrus"])
print()

# 8.3
f2e = dict()
for item in e2f.items():
    temp = {item[1] : item[0]}
    f2e.update(temp)

print(f2e)
print()

# 8.4
for item in e2f.items():
    if item[1] == 'chien':
        print(item[0])
        break
print()

# 8.5
print(e2f.keys())
print()


# 8.6
animals_dict = {"cats" : "Henri", "octopi" : "Grumpy", "emus" : "Lucy"}
plants_dict = {"aloe" : "first", "monstera" : "second", "Yucca" : "third"}
other_dict = {"germ" : "a"}
life = {"animals": animals_dict, "plants" : plants_dict, "other" : other_dict}

print(life.keys())

print(life['animals'].keys())

print(life['animals']['cats'])
print()

# 8.10
squares = {i: i*i for i in range(10)}
print(squares)