# 숫자 자료형
print(3 + 9)
print(3 * 7)
print(3 - 7)
print(3 / 7)

# 문자형
print("nadoCoding")
print('nadoCoding')

# boolean
print( 5 < 10 )
print( 5 > 10 )
print( not (5 > 10) )
print( not (5 < 10) )
# print( !(5 < 10) )  SyntaxError: invalid syntax 발생

# 변수
animal = "개"
name = "해피"
age = 3
message = "내가 키우는 애완동을은 " + animal + "이며 이름은 " + name + "이다"
print(message)

# str() : 자료형은 문자열로 바꿔주는 함수
message = "내가 키우는 애완동을은 " + animal + "이며 이름은 " + name + "이며 나이는 " + str(age) + "살이다."
print(message)

# ,(쉼표)로 문자열 연결
# 문자열 연결 시 형변환을 하지 않아도 되며 자동으로 값 사이에 공백이 추가된다.
message2 = "내가 키우는 애완동을은", animal, "이며 이름은", name, "이며 나이는", age, "살이다."
print("내가 키우는 애완동을은", animal, "이며 이름은", name, "이며 나이는", age, "살이다.")
print(message2)

# type() : 매개변수로 넣은 값이 어떤 타입인지 알려주는 함수
# int() : 문자열을 int 형으로 타입을 바꿔준다.
# float() : 문자열을 float 형으로 타입을 바꿔준다.
# str() :  정수형이나 실수형을 을 문자열로 타입을 바꿔준다.
print(type(int("3")))
print(type(float("3.5")))
print(type(str(3)))
print(type(str(3.5)))

"""
범위 주석 
print("str(3.5))
"""

#  ====================================== 실습 문제 =============================================
station = "사당"
message3 = station + "행 열차가 들어오고 있습니다."
print(message3)

station = "신도림"
message3 = station + "행 열차가 들어오고 있습니다."
print(message3)

station = "인천공항"
message3 = station + "행 열차가 들어오고 있습니다."
print(message3)

#  ====================================== 셀프체크  =============================================
"""
변수명은 status로 한다.
값은 변수에 '상품준비, 배송중, 배송완료' 순으로 저장한다.
"""
status = "상품 준비"
deliveryMessage = "배송상태 : "
print(deliveryMessage + status)

status = "배송 중"
print(deliveryMessage + status)

status = "배송 완료"
print(deliveryMessage + status)


"""

정리 :
파이썬은 js처럼 자료형을 앞에 명시하지 않아도 된다. 
특이했던 점은 부정논리 연산자가 !이 아니라 not 이라는 점이다.
또 + 로 문자열 연결을 할 경우 귀잖았던 공백 삽입을 ,로 연결하면 대신 해준다는 점이 좋았지만 
한 가지 주의할 점은 문자열을 + 연결하여 변수에 저장하면 문자열로 저장되지만 
message2 = "내가 키우는 애완동을은", animal, "이며 이름은", name, "이며 나이는", age, "살이다."
아직 파이썬에서의 배열은 공부하지 않았지만 아마 배열로 저장되는 것 같다. print(message2) 로 출력해 보면 
('내가 키우는 애완동을은', '개', '이며 이름은', '해피', '이며 나이는', 3, '살이다.')
이런 결과가 나오는 것을 확인 가능하다.

"""