'''
    작성일 : 2023년 09월 20일
    작성자 : 컴퓨터공학부 202395025 이준서
    설명 : 선택문 if-else
            교통 카드의 정류로 '청소년', '성인' 카드가 있다고 하자.
            사용자에게 카드의 종류를 입력받아 청소년이면 '청소년입니다.'
            '성인'이면 '성인입니다.'를 출력하자.
'''
# 1. 문자열를 입력받아 변수 card에 저장한다.
card = input("카드 종류(성인 or 청소년)를 입력 하시오 : ")
# 2. 만약 성인이면
print(":: 판단 1 ::")
if card == "성인":
#   1) "성인입니다."를 출력한다.
    print("성인입니다.")
# 3. 아니면
else :
#   1) "청소년입니다."를 출력한다
    print("청소년입니다.")

print(":: 판단 2 ::")
if card == "성인":
    print("성인입니다.")
if card == "청소년":
    print("청소년입니다.")
    

print(":: 판단 3 ::")
if card == "성인":      # if(card == '성인')
    print("성인입니다.")
elif card == "청소년":
    print("청소년입니다.")
else :
    print("잘못 입력 하였습니다.")