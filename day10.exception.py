# 예외

# 예외처리 구문
# try ~ except
# try:
#     num1 = int(input("한 자리 정수를 입력해 주세요."))
#     num2 = int(input("한 자리 정수를 입력해 주세요."))
# except ValueError:
#     print("ValueError 발생")
#
# try:
#     num1 = int(input("한 자리 정수를 입력해 주세요."))
#     num2 = int(input("한 자리 정수를 입력해 주세요."))
# except ValueError as e:
    # e 는 ValueError의 객체이다. print()로 객체를 출력하면 객체의 메서드인 __str__(self) 메서드가 자동으로 호출된다. toString() 같은 메서드,
    # print(e)


#     예외 발생시키기 raise
# try:
#     num1 = int(input("한 자리 정수를 입력해 주세요."))
#     num2 = int(input("한 자리 정수를 입력해 주세요."))
#     if num2 == 0:
#         raise Exception("Exception 예외 발생!")
# except ValueError:
#     print("ValueError 발생")
# except Exception as e:
#     print(e)

# 사용자 정의 exception 만들기
class My_exception(Exception):
    pass

#  아래 처럼 __메서드명__ 과 같은 메서드들은 스페셜 메서드라고 하며 특정한 역할이 정해진 메서드이다.
# __init__()은 초기화를 담당하며 __str__()은 print() 로 객체를 출력 시 자동으로 호출되는 매서드이다.
# class My_exception(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __str__(self):
#         return self.msg

# try:
#     num1 = int(input("한 자리 정수를 입력해 주세요 : "))
#     num2 = int(input("한 자리 정수를 입력해 주세요 : "))
#     if num2 == 0:
#         raise My_exception("My_exception 예외 발생!")
# except ValueError:
#     print("ValueError 발생")
# except My_exception as e:
#     print(e)

#  finally : try 종료 후 무조건 실행되는 부분으로 보통 파일을 닫거나 자원을 해제하는데 사용된다.
# try:
#     num1 = int(input("한 자리 정수를 입력해 주세요 : "))
#     num2 = int(input("한 자리 정수를 입력해 주세요 : "))
#     if num2 == 0:
#         raise My_exception("My_exception 예외 발생!")
# except ValueError:
#     print("ValueError 발생")
# except My_exception as e:
#     print(e)
# finally:
#     print("finally 호출됨!")

# ======================================================= 실습 문제 ===============================================================
# class SoldOutError(Exception):
#     pass
#
# chicken = 10
# waiting = 1
# MAXORDER = 10
#
# while True:
#     try:
#         if chicken == 0:
#             raise SoldOutError("재료가 소진돼 더 이상 주문을 받지 않습니다.")
#         print(f"[남은 치킨 : {chicken}]")
#         order = int(input("치킨을 몇 마리 주문하시겠습니까? "))
#         if order < 0 or order > 10:
#             raise ValueError
#         if order > chicken:
#             print("재료가 부족합니다.")
#         else:
#             print(f"[대기번호 {waiting}] {order}마리를 주문했습니다.")
#             waiting += 1
#             chicken -= order
#     except ValueError:
#         print("값을 잘못 입력했습니다.")
#     except SoldOutError as e:
#         print(e)
#         break

# ======================================================= 셀프 체크 ===============================================================
import sys
def save_battery(level):
    try:
        level = int(level)
        if level < 0:
            raise ValueError("음수값 입력")
        elif level <= 5:
            raise Exception(f"배터리 잔량 : {level}%\n배터리가 부족하여 스마트폰을 종료합니다.")
        elif level <= 30:
            print(f"배터리 잔량 : {level}%\n절전 모드로 사용합니다.")
        elif level > 100:
            raise ValueError("100초과 입력")
        else:
            print(f"배터리 잔량 : {level}%\n일반 모드로 사용합니다.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print()

save_battery(75)
save_battery(25)
save_battery("100")
save_battery("-10")
save_battery("120")
save_battery(3)

