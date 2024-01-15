x = 2
y = x + 5  # NameError: name 'x' is not defined
print(y)

# isinstance(객체, 자료형) 둘이 같으면 true, 다르면 false return
print(type(3.14))  # float
print((type(3.14)) == float)  # true
print(isinstance(3.14, float))  # true
print(isinstance("Inha", float))  # false
print(isinstance(55, float))  # false

artists = ['BTS', '뉴진스', '핑클', 'SES', 'HOT', '블랙핑크']
groups = artists  # 복제가 아니라 참조의 개념. 같은 곳을 바라보고 있기 때문
print(artists, groups)
groups[2] = '세븐틴'
print(artists, groups)


# 이건 immutable이어서 그런가??
# a = 1
# b = a
# print(a, b)  # 1 1
# b = 2
# print(a, b)  # 1 2