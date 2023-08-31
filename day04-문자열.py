# 문자열

message = """범위 안의 값들이 모두 
문자열로 인식 됩니다."""
print(message)

# 문자열 슬라이싱
# 문자열[사직 index : 종료 index] -> 시작 index 부터 종료 index - 1 까지의 문자열을 슬라이싱 한다.
# 문자열[:종료 index] -> 문자열[0:종료 index] 와 같은 의미이다.
# 문자열[시작 index:] -> 문자열[시작 index : 미자막 index] 와 같은 의미이다.
# 문자열[:] -> 모든 문자열을 의미한다.
jumin = "990229-1234567"
print(jumin[5])
print(jumin[0:5])
print(jumin[:5])
print(jumin[5:])
print(jumin[:])

# 문자열을 뒤에서 부터 슬라이싱 할 경우 음수 index를 사용한다.
# 음수 index는 jumin = "990229-1234567" 일 경우
# 맨 뒤부터 -1의 index를 가지고, 왼쪽으로 갈 수록 -2, -3 ... 식으로 증가한다.

# 문자열을 다루는 함수
# lower() : 소문자로 변환
# upper() : 대문자로 변환
# islower() : 소문자 인지 확인
# isupper() : 대문자 인지 확인
# replace() : 문자열 바꾸기
# index("찾는 문자열", start, end) : 찾는 문자열의 인덱스를 반환(없으면 오류 발생)
# find("찾는 문자열", start, end) : 찾는 문자열의 인덱스를 반환 (없으면 -1 반환)
# count() : 문자열이 나온 횟수 반환
# len() : 문자열의 길이를 출력해 준다.

message = "pyThon Study NadoCoDing"
print(message.lower())
print(message.upper())
print(message.islower())
print(message.isupper())
print(message.lower().islower())
print(message.lower().replace("python", "java"))
print(message.index("tu", 2)) # end 를 생ㄺ하면 start부터 끝까지 찾는다는 의미이다.
print(len(message))

# 서직 지정자
age = 22
print("저는 올해 %d살입니다." %age)

# format()
# 문자열 뒤에 .format()으로 연하고 {}에 매칭시킨다.
# 따로 index를 적어주지 않으면 순서대로 들어가며 index를 통해 위치를 바꿀 수 있다.
# index 뿐만 아니라 key=vlaue 형식으로 key 값을 지정하여 사용 가능하다.
print("{}, {}, {}" .format("문자열1", "문자열2", "문자열3"))
print("{0}, {1}, {2}" .format("문자열1", "문자열2", "문자열3"))
print("{2}, {1}, {0}" .format("문자열1", "문자열2", "문자열3"))
print("{key2}, {key1}, {key3}" .format(key1="문자열1", key2="문자열2", key3="문자열3"))

# f-string
# 미리 변수를 정의해 두고 문자열이 생성되기 전에 변수를 삽입해 문자열을 완성시킨다.
# 문자열 앞에 f를 붙여서 사용한다.
a = "싱싱한"
b = "사과"
print(f"{a} {b} 입니다.")

# \" \'
print(" \"  \' ")
print("  '  ' ")
print('  "  " ')
print("  \\    ")

# 문자열 앞에 r을 붙이면 /n과 같은 escape가 있더라도 무시하고 문자열로 출력한다.
print(r"C:\User\Nadocoding\Desktop")

# \r은 커서를 맨 앞으로 이동시켜 문자열을 덮어씌운다.
print("Coding\rnado")

# \b는 백스페이스와 같은 역할을 한다.
print("apple\b")

#  ============================================================== 실숩 문제 =======================================================
URL1 = "http://naver.com"
URL2 = "http://daum.net"
URL3 = "http://google.com"
URL4 = "http://youtube.com"

resource = URL1[7:len(URL1)-4]
result = resource[:3]+ str(len(resource)) + str(resource.count("e")) + "!"
print(f"{URL1}의 비밀번호는 {result}입니다.")

resource = URL2[7:len(URL2)-4]
result = resource[:3]+ str(len(resource)) + str(resource.count("e")) + "!"
print(f"{URL2}의 비밀번호는 {result}입니다.")

resource = URL3[7:len(URL3)-4]
result = resource[:3]+ str(len(resource)) + str(resource.count("e")) + "!"
print(f"{URL3}의 비밀번호는 {result}입니다.")

resource = URL4[7:len(URL4)-4]
result = resource[:3]+ str(len(resource)) + str(resource.count("e")) + "!"
print(f"{URL4}의 비밀번호는 {result}입니다.")

#  ============================================================== 셀프 체크 =======================================================
str1 = "the early bird catches the worm."
print(str1[0].upper() + str1[1:].lower())
print(str1.capitalize())

"""
정리:
파이썬에서의 문자열을 다루는 방법에 대해 학습했다. 
다른 언어에도 가지고 있는 함수와 중복되는 것들도 많았지만 파이선 만의 방식으로 되어져 있는 것들도 눈에 띄었다. 
확실이 다른 언어들보다 편리하다는 느낌을 받는다.
"""










