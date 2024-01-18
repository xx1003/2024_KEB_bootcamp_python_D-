# 9.1
# def good():
#     return ['Harry', 'Ron', 'Hermione']
# print(good())

def good(harry_potter):
    return harry_potter
print(good(['Harry', 'Ron', 'Hermione']))

# 9.2
def get_odds() -> list:
    """
    range(10)에서 홀수만 골라 리스트에 집어넣고 리스트 반환
    :return: list
    """
    return [i for i in range(10) if i % 2 != 0]

get_list = get_odds()
print(get_list[2])

# 9.3
def test(func):
    def inner(*args):
        print("start")
        func(*args)
        print("end")
    return inner

@test
def cout(*args):
    print(args)

cout(1,2,3)

# 9.4
class OopsException(Exception):
    print('Caught an oops')
talking = ['Yes', 'No', 'Hello', 'Oops']
for talk in talking:
    if talk == 'Oops':
        raise OopsException(talk)

try:
    raise OopsException('Caught an oops')
except OopsException as exc:
    print(exc)


