'''
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터공학부 202395025 이준서
    설명 : 반복을 제어하는 break, continue
            교재 137 페이지
            
    Test word : programming
'''
word = input("단어를 입력하세요 : ")

print(":: break1 ::")
for i in word:      # 입력한 단어에서 한글자씩 순차적으로 불러온다.
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":    # 만약 입력한 단어에서 모음이 나오면
        break       # 포함된 반복이 종료 (for문을 종료시킴)
    else :
        print(i, end="")    # 결과 예상 : pr 
        
print()
    
print(":: break2 ::")
for i in word:      # 입력한 단어에서 한글자씩 순차적으로 불러온다.
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:    # 만약 입력한 단어에서 모음이 나오면
        break       # 반복을 중단한다. 반복을 빠져 나간다.
    else :
        print(i, end="")
        
print()

print(":: continue ::")

for i in word:          # 입력한 단어에서 한글자씩 순차적으로 불러온다.
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        continue        # 반복의 시작으로 돌아간다. 아래의 문장을 만날 수 없다. | 반복을 계속한다.
    print(i, end="")    # 결과 예상 : prgrmmng