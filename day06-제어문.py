# 제어문
#  파이썬에서의 if 문

condition = 1 < 10
if condition:
    print("if")
elif condition:
    print("elif")
else:
    print("else")

print("\n")
# 파이썬에서의 for문
# 리스트나 튜플, 딕셔너리, 문자열들을 순ㅇ회할 시 사용
forTest = list(range(1, 10))
for element in forTest:
    print(element)

for element in [1, 2, 3, 4, 5]:
    print(f"이번 요소는 {element}입니다.")

# for (int i = 0; i < 10; i++) 과 같은 의미
mytext = ""
for index in range(10):
    mytext += str(index)
print(mytext)

mytext = ""
for index in range(0, 10, 2):    # 0부터 9까지 2씩증가
    mytext += str(index)
print(mytext)

# while 문
count = 0
while condition:
    count += 1
    if count == 10: break
    print("while문 입니다.")

# 콘솔입력 : input()
input = input("값을 입력하새요 : ")
print(input)

# list comprehension
# list를 바탕으로 변경된 새로운 리스트르 만들 때 사용한다.
baseList = [1, 2, 3, 4, 5]
newList = [element + 100 for element in baseList]
print(newList)

# list comprehension에 조건문을 사용해서 필터링 하는 예시
baseList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList = [element for element in baseList if element % 2 == 0]
print(newList)

# ============================================================ 실습문제 ============================================================
print("\n")
from random import *
count = 0
for index in range(0, 50):
    requiredTime = randint(5, 50)
    matchIngCondition = requiredTime >= 5 and requiredTime <= 15
    if matchIngCondition:
        successMessage = f"[0] {index}번째 손님 (소요시간 : {requiredTime}분)"
        print(successMessage)
        count += 1
    else:
        failMassage = f"[] {index}번째 손님 (소요시간 : {requiredTime}분)"
        print(failMassage)
print(f"총 탑승객 : {count}명")

# ============================================================ 셀프체크 ============================================================
print("\n")
purchasedQuantity = 0
while purchasedQuantity < 6:
    message = "2+1 상품입니다."
    print(message)
    purchasedQuantity += 1

totalPrice = (purchasedQuantity - purchasedQuantity // 3) * 1000
print(f"총 가격은 {totalPrice}원입니다.")







