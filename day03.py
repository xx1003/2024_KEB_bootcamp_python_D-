course = "* KEB 2024# KEB !Bootcamp KEB...*!#"
print(course.find("KEB"))  # 제일 먼저 찾은 거 리턴
print(course.rfind("KEB"))  # reverse find
print(course.index("KEB"))
print(course.rindex("KEB"))
print(course.find("INHA"))  # -1
print(course.index("INHA"))  # ValueError: substring not found

print(course)
course = course.replace('KEB','INHA',2)
print(course)
print(course.strip())
print(course.strip("!#*"))  # 양쪽 끝에 연속된 애들만 지워짐. 중간 애들 안 지워짐.

# print(course)
# print(course.replace('KEB','INHA'))
# print(course)  # 안바뀜. immutable
# course = course.replace('KEB','INHA')  # 부분은 할당 안 되지만, 전체는 바꿀 수 있음.
# print(course)