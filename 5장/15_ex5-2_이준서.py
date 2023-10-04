'''
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터공학부 202395025 이준서
    설명 : 1. 두 수를 입력 받아 두 수 사이의 합계 출력하기
           2. 두 수 사이의 짝수의 합계 출력하기
            심화문제 5.2, 141쪽
'''
num1 = int(input("첫번째 수 입력 : "))
num2 = int(input("두번째 수 입력 : "))
total1 = 0
total2 = 0
while True:                             # num1이 num2보다 작을때
    if num1 < num2:
        for i in range(num1,num2+1):    # num1부터 num2까지 반복하면서
            total1 += i                 # total1에 계산한 값을 저장한다.
        print("두 수 사이의 합계 : ",total1)
        for i in range(num1, num2 +1):  # num1부터 num2까지 반복하면서
            if i % 2 == 0:              # i를 2로 나눈 나머지가 0이면
                total2 += i             # total2에 계산한 값을 저장한다.
        print("두 수 사이의 짝수의 합계 : ",total2)
        break
    else:
        break
print("다시 입력하세요")