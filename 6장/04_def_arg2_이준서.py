'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 202395025 이준서
    설명 : 여러개의 값을 넘겨주고 여러개의 값을 돌려 받기.

    두 수를 전달하여 사칙연산의 결과값을 돌려주는 함수.
    
    [알고리즘]
    (함수)
        3. 두 수를 전달받아 매개변수에 저장한다.
        4. 두 수의 사칙연산을 계산한다.
        5. 계산된 결과값을 돌려준다.

    (메인)
        1. 두 수를 입력 받는다.
        2. 두 수를 가지고 함수를 호출한다.
        6. 돌려받은 값을 출력한다.
'''

# 함수 선언
def calculator(num1,num2):
    add = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    divide = num1 / num2
    rest = num1 % num2
    return add, sub, mult, divide, rest
    
# 메인
num1 = int(input("첫번째 수 : "))
num2 = int(input("두번째 수 : "))

sum, sub, mult, divide, rest = calculator(num1,num2)
print(f"{num1} + {num2} = {sum}")
print(f"{num1} - {num2} = {sub}")
print(f"{num1} * {num2} = {mult}")
print(f"{num1} / {num2} = {divide}")
print(f"{num1} % {num2} = {rest}")