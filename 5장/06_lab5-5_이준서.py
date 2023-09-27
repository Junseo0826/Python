'''
    작성일 : 2023년 09월 27일
    작성자 : 컴퓨터공학부 202395025 이준서
    설명 : 반복문으로 팩토리얼 구하기.
'''
num = int(input("정수를 입력하시오: "))
pact = 1
for i in range(1, num+1):
    pact *= i
print(f"{num}!은 {pact}이다.")