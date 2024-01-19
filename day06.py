class FlyingMixin:
    def fly(self):
        return f"{self.name}이(가) 하늘을 훨훨 날아갑니다~"


class SwimmingMixin:
    def swim(self):
        return f"{self.name}이(가) 수영을 합니다."


class Pokemon:
    def __init__(self, name):
        self.name = name


class Charizard(Pokemon, FlyingMixin):
    pass


class Garados(Pokemon, SwimmingMixin):
    pass


g1  = Garados("갸라도스")
c1 = Charizard("리자몽")

print(g1.swim())
print(c1.fly())
