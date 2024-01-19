def get_odds(n):
    for i in range(1, n+1, 2):
        yield  i

cnt = 0
odds = get_odds(9)
for odd in odds:
    cnt = cnt +1
    if cnt == 3:
        print(f'Third number is {odd}')
        break