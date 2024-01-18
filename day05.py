# Closure
def out_func(nout):
    def in_func():
        return nout * nout
    return in_func


x = out_func(9)  # 내부 함수 리턴? 그래서 x 는 함수 (inner function 주소를 받음)
print(type(x))
print(x)
print(x())

# Inner function
# def out_func(nout):
#     def in_func(nin):
#         return nin * nin
#     return in_func(nout)
#
# print(out_func(5))