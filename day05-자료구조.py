# 자료구조

# 리스트
# 생성방법 :  변수명 = []
# 서로 다른 자료형도 저장가능하다.
mylist = [1, "2", 3]

# append(value) : 맨 마지막 index에 값을 추가한다.
# pop() : 맨 마지막 index의 값을 삭제한다.
# insert(index, value) : index에 값을 넣는다.
# sort() : 오름차순으로 정렬한다.
# sort(reverse=True) : 내림차순으로 정렬한다.
# reverse() : 리스트의 값을 뒤집는다.
# sorted(list) : sort() 는 원본 리스트르 변경하지만 sorted()는 원본 리스트를 변경하지 않고 정렬된 새로운 리스트를 반환한다.
# extend(otherList) : list뒤에otherList를 붙여서 확장시킨다.
# count(valye) : list안에서 value의 갯수를 반환한다.
# clear() : 모든 값들 삭제

mylist.append("4")
print(mylist)

mylist.pop()
print(mylist)

mylist.insert(1, "insr")
print(mylist)

# 서로 다른 자료형이 있으면 sort() 불가능
mylist.clear()
mylist.append(4)
mylist.append(6)
mylist.append(1)
mylist.append(3)
mylist.sort()
print(mylist)

mylist.sort(reverse=True)
print(mylist)

print(sorted(mylist))
print(sorted(mylist).count(1))

list2 = ["!", "2", "3"]
mylist.extend(list2)
print(mylist)

# 딕셔너리 : kdy, value 로 이루어진 자료구조를 의미한다. (=map)
# 빈 딕셔너리 생성
mydictionary = {}

# 예시
mydictionary2 = {1: "값1", 100: "값2", "문자열kdy": 1500}
print(mydictionary2)

# 값 가져오기
# 1. 딕셔너리명[key] : key에 맞는 값을 반환한다. 만약 key에 해당하는 value가 없으면 KeyError 를 발생시킨다.
# 2. get(key) :  key에 맞는 값을 반환한다. 만약 key에 해당하는 value가 없으면 None를 출력한다.
#                이 때, None 대신 다른 값을 출력시키고 싶다면 get(key, "대체값") 이런 식으로 두번째 인자에 default 값을 넘겨주면 된다.

# print(dictionary2[24234])    오루 발생
print(mydictionary2.get(24234))
print(mydictionary2.get(23241, "대체값"))

# in 연산자 : 해당 kdy가 딕셔너리 안에 존재하는지 확인할 때 사용한다. kdy가 있으면 true, 없으면 false를 반환한다.
# 또한 in 연산자는 문자열 안에 찾는 문자열이 존쟈하는지 확인할 경우에도 사용이 가능하다.
print(3 in mydictionary2)
print("가나다" in "나다라마가나다")

# 딕셔너리에 값 추가/수정하기
# 딕셔너리에 값을 추거/수정하는 작업은 모두 [] 를 통해 이루어진다.
# ex) dictionary["key"] = value 를 할 경우 key가 존재하면 수정, 없으면 추가가 된다.

mydictionary[1] = "ㅁㄴㅇㅁㄴㅇ"
mydictionary[2] = "sdsvbnbn"
mydictionary[2] = "대체"
print(mydictionary)

# keys() : 딕셔너리의 모든 ksy들을 반환
print(mydictionary.keys())

# values() : 딕셔너리의 모든 value들을 반환
print(mydictionary.values())

# items() : 딕셔너리의 모든 kdy.value들을 쌍으로 반환
print(mydictionary.items())

# clear() : 딕셔너리 비우기
mydictionary.clear()
print(mydictionary)

# 튜플 : 한번 생성하고 나면 readOnly 이다.
# 다만 리스트에 비해 읽기 성능이 좋다.

# 튜플 생성 방법
mytuple = ("가", "나", "다")
print(mytuple)
print(mytuple[0])
print(mytuple[1])
print(mytuple[2])

(key1, key2, key3) = ("값1", "값2", "깂3")
print((key1))
print((key1, key2))
(newKdy1, newKdy2,newKdy3) = (key3, key2, key1)
print((newKdy1, newKdy2,newKdy3))

# 튜플도 슬라이싱이 가능하다.
print(mytuple[:1])

# 세트 : 중복을 허용하지 않고 순서를 보장하지 않는 자료구조이다.
mySet = {"1", "2", "3", "!", "1"}
print(mySet)  # {'1', '2', '!', '3'}
mySet1 = set([1, 2, 3, 1, "!"])
print(mySet1)

# 교집합 연산자 &
# 교집합 함수 intersection()
print( mySet.intersection(mySet1) )
print( mySet & mySet1 )

# 합집합 연산자 |
# 합집합 함수 union
print( mySet.union(mySet1) )
print( mySet | mySet1 )

# 차집합 연산자 -
# 차집합 함수 difference()
print( mySet.difference(mySet1) )
print( mySet - mySet1 )

# set에 추가 add()
mySet.add("추가된 값")
print(mySet)


# 자료구조 변환하기
print(type(mySet))

# 리스트로 변환하는 방법
mylist2 = list(mySet)
print(type(mylist2))

# 튜플로 변환하는 방법
mytuple = tuple(mySet)
print(type(mytuple))

# 세트로 변환하는 방법
toSet = set(mylist2)
print(type(toSet))


# ============================================================= 실습문제 ==============================================================
from random import *
# range() 는 start부터 end-1 까지의 값들을 생성해 준다.
members = list(range(1, 21))
print(members)

# fhuffle(list) 은 말 그대로 리스트를 셔플해 준다.
shuffle(members)
print(members)

# sample(list, num) 은 리스트에서 중복값 없이 랜덤한 값을 뽑는 함수이다.
result = sample(members, 4)
print(result)
# 결과
message = f"""--당첨자 발표--\n치킨 당첨자 : {result[0]}\n커피 당첨자 : {result[1:]}\n-- 축하합니다! --"""
print(message)

# ============================================================= 셀프 체크 ==============================================================
print("\n")
subjects = ["자료구조", "알고리즘", "컴퓨터구조", "알고리즘","객체지향 프로그래밍", "데이터베이스","네트워크", "데이터베이스"]
result2 = set(subjects)
message2 = f"""신청하신 과목은 다음과 같습니다.
{result2}"""
print(message2)


"""
정리:
[] : 리스트
{} : 세트 하지만 , key:value형식이면 딕셔너리 
() : 튜플 

리스트의 특징 : 순서보장, 값의 중복을 혀용 
세트의 특징 : 순서보장 x, 중복값 혀용 x 
튜플의 특징 : 한번 생성하면 변경불가 -> readOnly 하지만 읽기 속도가 빠름
딕셔너리의 특징 : key:valye쌍 key 값으로 value를 찾음 
"""



