import random

class OopsException(Exception):
    pass

# numbers = list()
# for i in range(5):
#     numbers.append(random.randint(1, 100))
numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

try:
    pick = int(input(f"Input index (0 ~ {len(numbers)-1}) : "))
    print(numbers[pick])
    print(5//2)
    raise OopsException("Oops")  # exception 예외 강제 발생
except IndexError as err:
    print(f"Wrong index number\n{err}")
except ValueError as err:
    print(f"Input Only Number~\n{err}")
except ZeroDivisionError as err:
    print(f"The denominator cannot be 0.\n{err}")
except OopsException as err:
    print(f"Oops Oops {err}")
except Exception as err:
    print(f"Error occurs : {err}")
else:
    print(f"Program terminate")