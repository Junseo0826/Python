'''
    작성일 : 2023년 09월 13일
    작성자 : 컴퓨터공학부 202395025 이준서
    설명 : 직각 삼각형의 빗변의 길이를 구하시오.
'''
base = int(input("밑변의 길이 : "))
height = int(input("높이의 길이 : "))
area = (base**2 + height**2)**(1/2)
print("밑변의 길이가 {}, 높이의 길이가 {}인 삼각형의 넓이 : {}". format(base,height,area))