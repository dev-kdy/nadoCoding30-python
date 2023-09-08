# 표준 입출력

# print(출력할 내용, sep=" ", end="\n", file=None, flush=False)
# sep 은 separator의 약자로 출력 내용을 , 구분시 , 대신에 들어갈 값을 의미한다.
print("sep", "테스트", sep="    ")    # 구분자로 들여쓰기를 주었다.

# end 는 출력 종료 후 나올 문자열을 의미한다. 기본은 \n으로 줄바꿈이지만 이것도 재정의가 가능하다.
print("sep", "end", "테스트", sep="    ", end="!")    # 구분자로 들여쓰기를 주었다.    end를 !로 재정의 했다.

import sys
print("파이썬", "자바", file=sys.stdout)
print("파이썬", "자바", file=sys.stderr)

print()
# ljust(a) : a 만큼 공간 확보를 한 뒤 왼쪽에서 부터 채운다.
# rjust(a) : a 만큼 공간 확보를 한 뒤 오른쪽에서 부터 채운다.
# zfill(a) : a 만큼 공간 확보를 한 뒤 문자열의 남는 공간은 0으로 채운다.

scores = {"수학": 100, "영어": 50, "코딩": 100}
# for subject, score in scores.items():
#     print(subject.ljust(6), str(score).rjust(5), sep=":", end="점\n")

for num in range(1, 21):
    print("대기번호 :", str(num).zfill(5))

# .format() : 알맞은 {} 에 지정된 값을 넎는다.
# {0: >10} 은 10칸을 확보한 뒤 format 0번째 값을 오른족에서부터 채우고 남은 칸들은 빈칸으로 채운다는 의미이다.
print("{0: >10}".format(500))
print("{0:_<100}".format(500))
# format 값에 숫자를 넣을 경우 {0:_<+100} 처럼 자릿수 앞에 + 를 붙이면 양수일 경우에 +를 붙인 채로 결과가 나온다.
print("{0:_<+100}".format(500))
print("{0:_<+100}".format(-500))
# print("{0:_<+100}".format("문자열")) -> 오류 발생 문자열일 경우에는 불가능
print("{0:,}".format(1000000000))     # 1,000,000,000
print("{0:+,}".format(1000000000))    # +1,000,000,000
print("{0:+,}".format(-1000000000))   # -1,000,000,000

print("{0:.2f}".format(5 / 3))    # 소수점 2자리까지만 출력한다는 의미

# 파일 입출력
# open("파일명", "모드", encoding="인코딩 형식")
# mode 종류 :
# r : 읽기
# w : 쓰기 (덮어쓰기)
# a : 이어쓰기
# write() : 지정 파일에 쓰는 메서드
# close() : 파일을 닫아주는 메서드
score_file = open("score.txt", "w", encoding="utf8")
for subject, score in scores.items():
    print(subject.ljust(6), str(score).rjust(5), sep=":", end="점\n", file=score_file)
score_file.close()
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("{0: <6}:{1: >5}점\n".format("과학", 80))
score_file.close()

# read() : 파일 전체 읽기
score_file = open("score.txt", "r", encoding="utf8")    # 읽기 모드로 파일 열기
text = score_file.read()    # 파일 전체 내용 저장
print(text)
score_file.close()
# readline() : 한줄 읽고 커서는 다음줄로 이동
score_file = open("score.txt", "r", encoding="utf8")    # 읽기 모드로 파일 열기
text = ""
while True:
    line = score_file.readline()
    if not line:
        break
    text += line
print(text)
score_file.close()
# readlines() : 파일의 모든 내용을 읽어서 리스트 형태로 반환
score_file = open("score.txt", "r", encoding="utf8")
for line in score_file.readlines():
    # 한줄씩 리스트 형태로 저장, 타입은 문자열
    print("{0}".format(str(type(line))),line, end="")
score_file.close()

# pickle 모듈 : 프로그램에서 사용하는 데이터를 파일 형태로 저장하거나 불러올 수 있게 하는 모듈
# dump(저장할 데이터, 저장할 파일명) : 해당 파일에 데이터를 바이더리 형태로 저장한다.
# load(불러올 파일명 ) : 파일을 불러온다.
import pickle
# 파일을 바이너리로 읽거나 쓰기를 할 경우엔 txt파일과 구분을 위해 뒤에 b를 붙인다.
# 예시) rb, wb
profile_file = open("profile.pickle", "wb")
profile = {"이름": "스누피", "나이": 30, "취미": ["축구", "코딩", "골프"]}
print(profile)
pickle.dump(profile ,profile_file)
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

# with 문 : 파일을 열고 나서 close()를 대신 호출해 준다.
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

profile_text = {}
with open("profile.pickle", "rb") as profile_file:
    profile_text = pickle.load(profile_file)

with open("profile.txt", "w", encoding="utf8") as profile_file:
    profile_file.write(str(profile_text))

# ========================================================== 실습 문제 =============================================================
for week in range(1, 51):
    report = "- {0}주차 주간보고 -\n부서 : \n이름 : \n업무 요약 : \n".format(week)
    with open(f"{week}주차.txt", "w", encoding="utf8") as report_file:
        report_file.write(report)

# ========================================================== 셀프 체크 =============================================================
with open("class.txt", "w", encoding="utf8") as class_file:
    class_file.write("초록반 5세 20명 파랑반 6세 18명 노랑반 7세 22명")

with open("class.txt", "r", encoding="utf8") as class_file:
    class_text = class_file.read()
    result_text = ""
    for word in class_text.split():
        result_text += word
        if word.endswith("명"):
            result_text += "\n"
        else:
            result_text += " "

print(result_text)

