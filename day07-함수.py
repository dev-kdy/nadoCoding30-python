# 함수

# def 키워드를 통해 함수를 정의한다.

def add(num1, num2):
    return num1 + num2

print(add(1, 10))


# 파라미터에 default 값 주기
def add2(num1=0, num2=0):
    return num1 + num2

print(add2(1))

# 반환값이 여러 개일 경우에는 튜플로 반환한다.
def test(num1, num2, str3):
    return num1 + num2, str3

print(test(1, 10, "테스트"))
result1, result2 = test(2, 100, "문자열")
myTuple = test(2, 100, "문자열")
print(myTuple)

# 키워드 인자
# 함수 사용 시 인자에 키워드르 붙여서 순서 상관없이 사용이 가능하다.
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(age="22", name="yyeeoop", main_lang="Java")

# print() 의 매개변수중 end의 default 값이 \n으로 되어져 있어서 출력 후 줄바꿈을 하는것 이게 마음에 안든다면 print() 호출 시 end 를 다른 값으로 변경 가능.

def profile2(name, age, lang1, lang2, lang3, lang4, lang5):
    print(f"이름 : {name}\t나이 : {age}\t", end=" 언어들 :  ")
    print(lang1, lang2, lang3, lang4, lang5)

profile2("yyeeoop","22", "C", "C++", "Java", "Javascript", "Python")

# 가변인자 사용법 : *변수명
# def func(*param):
# 자바에선 가변인자를 배열로 받지만 파이썬에서는 튜플로 받는다.

def test2(*parms):
    print(type(parms))
    print(parms)

test2("가", "나", "다", "라")

# 함수 내에서 전역변수를 사용할 경우에는 전역변수임을 할리는 키워드인 global을 붙인다.

my_global = 10
def globalTest():
    global my_global  # 이 줄 아래에서 사용하는 my_global은 전역분수이다.
    my_global = 20

globalTest()
print(my_global)

# ======================================================== 실습 문제 =========================================================
height = 175
gender = "남"
def std_weight(height=0, gender="남"):
    if gender == "남":
        return round((height/100)**2 * 22, 2)
    else:
        return round((height/100)**2 * 21, 2)

print(f"키 {height}cm 남자의 표준 체중은 {std_weight(height, gender)}입니다.")

# ======================================================== 셀프 체크 =========================================================
def get_air_quality(fine_dust):
    result = ""
    if fine_dust < 31:
        result = "좋음"
    elif fine_dust > 30 and fine_dust < 81:
        result = "보통"
    elif fine_dust > 80 and fine_dust < 151:
        result = "나쁨"
    else:
        result = "매우 나쁨"
    return result

print(get_air_quality(15))
print(get_air_quality(151))



# 함수

# def 키워드를 통해 함수를 정의한다.

def add(num1, num2):
    return num1 + num2

print(add(1, 10))


# 파라미터에 default 값 주기
def add2(num1=0, num2=0):
    return num1 + num2

print(add2(1))

# 반환값이 여러 개일 경우에는 튜플로 반환한다.
def test(num1, num2, str3):
    return num1 + num2, str3

print(test(1, 10, "테스트"))
result1, result2 = test(2, 100, "문자열")
myTuple = test(2, 100, "문자열")
print(myTuple)

# 키워드 인자
# 함수 사용 시 인자에 키워드르 붙여서 순서 상관없이 사용이 가능하다.
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(age="22", name="yyeeoop", main_lang="Java")

# print() 의 매개변수중 end의 default 값이 \n으로 되어져 있어서 출력 후 줄바꿈을 하는것 이게 마음에 안든다면 print() 호출 시 end 를 다른 값으로 변경 가능.

def profile2(name, age, lang1, lang2, lang3, lang4, lang5):
    print(f"이름 : {name}\t나이 : {age}\t", end=" 언어들 :  ")
    print(lang1, lang2, lang3, lang4, lang5)

profile2("yyeeoop","22", "C", "C++", "Java", "Javascript", "Python")

# 가변인자 사용법 : *변수명
# def func(*param):
# 자바에선 가변인자를 배열로 받지만 파이썬에서는 튜플로 받는다.

def test2(*parms):
    print(type(parms))
    print(parms)

test2("가", "나", "다", "라")

# 함수 내에서 전역변수를 사용할 경우에는 전역변수임을 할리는 키워드인 global을 붙인다.

my_global = 10
def globalTest():
    global my_global  # 이 줄 아래에서 사용하는 my_global은 전역분수이다.
    my_global = 20

globalTest()
print(my_global)

# ======================================================== 실습 문제 =========================================================
height = 175
gender = "남"
def std_weight(height=0, gender="남"):
    if gender == "남":
        return round((height/100)**2 * 22, 2)
    else:
        return round((height/100)**2 * 21, 2)

print(f"키 {height}cm 남자의 표준 체중은 {std_weight(height, gender)}입니다.")

# ======================================================== 셀프 체크 =========================================================
def get_air_quality(fine_dust):
    result = ""
    if fine_dust < 31:
        result = "좋음"
    elif fine_dust > 30 and fine_dust < 81:
        result = "보통"
    elif fine_dust > 80 and fine_dust < 151:
        result = "나쁨"
    else:
        result = "매우 나쁨"
    return result

print(get_air_quality(15))
print(get_air_quality(151))

"""
정리:
파이썬에서는 반환값을 여러개 반환할 경우 튜플로 반환된다.
함수 사용시 func(arg_name1="value") 이런 식으로 인자의 키워드를 붙여서 순서 상관 없이 안자를 넣을 수 있다. 이를 키워드 인자라고 한다.
가변인자는 변수명 앞에 *를 붙여서 사용하며 함수 내에서 튜플로 사용이 가능하다.
"""

