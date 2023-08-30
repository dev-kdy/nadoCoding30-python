# 파이썬스러운 연산자

# / 연산자는 실수형으로 리턴한다.
#  만약 몫을 얻고 싶다면 // 를 사용해야 한다.
print(10 / 2)  # 5.0
print(10 // 2) # 5

# ** 연산자는 거듭제고 연산자이다
print(2 ** 5) # 32

# mod 연산자는 % 로 동일하다.

#  논리 연산자
#  && , || , ! 이 아니라 and , or, not 으로 사용한다.
# 하지만 != 은 그대로 != 이다.

# abs(a) : 절대값 함수
# pow(a, b) : 거듭제곱 함수
# max(a, b, c) : 가장큰값
# min(a, b, c) : 가장작은값
# round(a) : 두번째 매개변숙가 없으면 소수점 첫째자리에서 반올림
# round(a, b) : 두번째 매개변숙가 있으면 b의 값의 자리까지 반올림해서 나타냄

print(abs(-10))
print(pow(10, 2))
print(max(-10, 1, 150))
print(min(-10, 1, 100))
print(round(12.123))
print(round(12.123, 2))
# print(floor(12.123, 2))

# 모듈 : 어떤 기능들을 모아놓은 파이썬 파일
# from 모듈령 import 기능

from math import *

# floor() math 모듈에 있느 기능이라 import를 해야 사용 가능하다.
# floor(a): 내림
# ceil(a) : 올림
# sqrt(a) : 재곱근
print(floor(12.123))
print(ceil(12.123))
print(sqrt(144))

# from math import * 과 from math 의 차이점
# 둘 다 math 모듈의 모든 기능을 사용할 수 있지만 from math import * 은 함수명 앞에 모듈명을 붙이지 않아도 되지만
# from math 은 math 모듈의 함수를 사용할 경우 math.floor() 처럼 앞에 모듈명을 붙여줘야 한다.
# 특정 함수만 사용할 경우 from math import floor, ceil 이런 식으로 함수명을 나열하면 된다.

# random() : 난수 생성 0 ~ 1 사이
# randrange(a, b) : a 익상 b 미만의 정수형 난수 생성
# randint(a, b) : a 익상 b 이하의 정수형 난수 생성
from random import *
print(random())
print(randrange(10, 100))
print(randint(10, 500))

# ================================================== 실습 문제 ======================================================
message = "오프라인 스터디 모임 날짜는 매월 " + str(randint(3, 28)) + "일로 선정됐습니다."
print(message)

# ================================================== 셀프체크 =======================================================
# 섭씨 온도가 30 도일때
clsius = 30
fahrenheit = ( clsius * 9 / 5 ) + 32
temperatureMsg = "섭씨 온도: " + str(clsius) + "\n화씨온도 : " + str(fahrenheit)
print(temperatureMsg)

print("\n ------------------------ ")
# 섭씨 온도가 10 도일때
clsius = 10
fahrenheit = ( clsius * 9 / 5 ) + 32
temperatureMsg = "섭씨 온도: " + str(clsius) + "\n화씨온도 : " + str(fahrenheit)
print(temperatureMsg)


"""
정리: 
파이썬에서의 모듈 사용법과 import에 대해서 배웠다. 모듈 math와 random에 정의된 몇가지 기능들에 대해서 알아보았으며,
다른 언어들과 파이썬 파이썬 연산자들중 다른 연산자들에 대해 학습했다. 
"""


