class FlyingMixin:
    def fly(self):
        return f"{self.name}이(가) 하늘을 훨훨 날아갑니다~"


class SwimmingMixin:
    def swim(self):
        return f"{self.name}이(가) 수영을 합니다."


class Pokemon:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print("공격")


class Charizard(Pokemon, FlyingMixin):
    pass


class Garados(Pokemon, SwimmingMixin):
    pass


g1 = Garados("갸라도스")
c1 = Charizard("리자몽")
# print(g1.swim())
# print(c1.fly())
# c1.attack()
# # Charizard.attack()  # 에러 남
# Charizard.attack(c1)
print(g1.name)
g1.name = "잉어킹"
print(g1.name)
