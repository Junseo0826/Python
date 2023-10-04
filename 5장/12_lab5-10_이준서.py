'''
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터공학부 202395025 이준서
    설명 : 사용자가 입력하는 숫자의 합을 계산
            교재 132 페이지
'''
'''
total = 0                                   # 합계
yes_or_no = "yes"
while yes_or_no == "yes":                   # 조건
    num = int(input("숫자를 입력하시오: "))
    yes_or_no = input("계속?(yes/no): ")
    total = num + total                     # 합계 계산
    if yes_or_no == "no":                   # 조건식
        break
print("합계 :",total)                       # 합계 출력
'''
total = 0                                       # 합계
yes_or_no = "yes"                               # 조건
while yes_or_no == "yes":                       # 조건식
    num = int(input("숫자를 입력하시오: "))      # 숫자입력  
    total += num                                # 합계 계산
    yes_or_no = input("계속?(yes/no): ")        # yes를 입력받으면 계속한다.
print('합계 : ',total)