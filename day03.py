# preview
subjects = "python c++ database linux"
print('%e' % (0.7045))

print(subjects.isalnum())  # 알파벳 또는 숫자로만. 띄어쓰기도 X
subject = input("수강신청과목 입력 : ")

try:
    print(f"해당 과목은 존재합니다. 위치는 {subjects.index(subject)}번 인덱스입니다.")
except ValueError:
    print('해당과목이 존재하지 않습니다.')
