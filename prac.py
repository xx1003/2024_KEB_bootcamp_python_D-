start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop","get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"

for start in start1:
    start = start.title()

print(start1)
'! '.join(start1)