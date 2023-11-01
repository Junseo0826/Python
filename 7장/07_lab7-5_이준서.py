'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 202395025 이준서
    설명 : LAB 7-5 함수는 튜플을 돌려줄 수 있다.
    
        반지름을 입력받아 원의 넓이와 둘레를 계산하시오.
        넓이와 둘레를 계산하는 함수를 작성하시오.
        함수는 넓이와 둘레를 함께 돌려줍니다. (return)
        
        [함수]
            3. 반지름을 받아서 매개변수에 저장한다.
            4. 넓이와 둘레를 계산한다.
            5. 넓이와 둘레를 돌려준다.(함수를 호출한 곳으로)
                return 넓이, 둘레
            
        [메인]
            1. 반지름을 입력 받는다.
            2. 함수 호출 -> 반지름을 가지고 호출한다.
            6. 돌려받은 넓이와 둘레를 튜플로 저장한다.
            7. 출력한다.
'''
import math


def area(r):
    area = r * r * math.pi
    circum = 2 * r * math.pi
    return area, circum

radius = float(input("원의 반지름? "))
(area, circum) = (area(radius))
print(f"반지름이 {radius}인 원의 넓이 {area:.2f}, 원의 둘레{circum:.2f}")

circle = area(radius)
print(f"반지름이 {radius}인 원의 넓이 {circle[0]:.2f}, 원의 둘레{circle[1]:.2f}")
