# Class

# 클래스 생성법
# 생성자의 이름은 __init__으로 고정
# 메서드의 첫 번째 파라미터는 무조건 self가 와야 한다.
# 인스턴스 변수를 초기화 할 경우 self.a 이런 식으로 self를 통해 접근 가능
# 추 후 인스턴스를 생성 하고나서 나중에 인스턴스 변수를 추가할 수 있다.
# 그럴 경우 인스턴스명.추가할인스턴스변수이름 = 값 이런 식으로 추가환다.
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def my_method(self):
        print(self.a, self.b)

test = Test(10, 100)
test.my_method()

test.c = 1000
print(test.c)

# 상속
# 상속 시 클래스명(상속받을 클래스1, 상속받을 클래스2...) 이런식으로 상속받는다. 또한 다중 상속이 가능하다.
# 메서드 오버라이딩, 메서드 오버로딩 지원
# super() 사용시 주의사항
# 1. 다중 상속 시 super()은 처음 상속받은 클래스를 의미하므로 다중 상속 시 에는 직접 클래스 명을 명시 해 주어야 한다.
# 2. super().__init__()으로 부모 클래스의 생성자를 호출 할 경우에는 첫 번째 인자로 self넣지 말아야 한다.
class Test2(Test):
    def __init__(self, a, b, c, d, e):
        # Test.__init__(self, a, b)  # 부모 클래스 초기화
        # 아래와 같은 의미이다.
        super().__init__(a, b)
        self.c = c
        self.d = d
        self.e = e

    # 메서드 오버라이딩
    def my_method(self):
        print(self.a, self.b, self.c, self.d, self.e)

    def my_pass(self):
        pass

test2 = Test2(10, 11, 12, 13, 14)
test2.my_method()
test2.my_pass()
print("전 줄에 pass 호출 완료")


class Test3(Test2):
    #     클래스 변수 생성방법
    class_variable = "클래스 변수입니다."

    def __init__(self, a, b, c, d, e, f):
        super().__init__(a, b, c, d, e)
        self.f = f

    def my_method(self):
        super().my_method()
        print(self.f)

test3 = Test3(10, 11, 12, 13, 14, 15)
test3.my_method()
print(Test3.class_variable)

# ========================================================== 실습 문제 ===========================================================
print()
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print("{} {} {} {}원 {}년".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))


house_list = []
house_list.append(House("강남", "아파트", "매매", "10억", 2010))
house_list.append(House("마포", "오피스텔", "전세", "5억", 2007))
house_list.append(House("송파", "빌라", "월세", "500/50만", 2000))

print("총 3가지 매물이 있습니다.")
for house in house_list:
    house.show_detail()

# ========================================================== 셀프 체크 ===========================================================
print()
class ParkingManager:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        print(f"총 {capacity}대를 등록할 수 있습니다.")

    def resister(self):
        if self.count >= self.capacity:
            print("더 이상 등록할 수 없습니다.")
            return
        self.count += 1
        print(f"차량 신규 등록 ( {self.count}/{self.capacity} )")

manager = ParkingManager(5)
for i in range(7):
    manager.resister()
