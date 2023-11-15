'''
    작성일 : 2023년 11월 15일
    작성자 : 컴퓨터공학부 202395025 이준서
    설명 : LAB 9-2 : 트위터 메세지 처리의 단어 추출
        띄어쓰기로 문자열을 분리하고, 단어의 개수를 찾아라.
'''
text = "There's a reason some people are working to make it harder to vote, \
        especially for people of color. \
        It's because when we show up, things change."
# 띄어쓰기로 문자열을 분리하고, 단어의 개수를 찾아라.
# len() => 길이(개수) : 리스트의 항목 개수 찾는 함수
text2 = text.split()
print(text2)
print(len(text2))

# 도전문제 9.1
# 회사 이름은 **로 표시
# KT, Samsung, LG, SKT
text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG \
U+ Mystic Pink 30%, SKT Mystic Blue not disclosed) '
# text = text.replace('SKT','**')
# text = text.replace('KT','**')
# text = text.replace('LG','**')
# text = text.replace('Samsung','**')
# print(text)

lower_text = text.lower()
replace_word = ['kt','samsung','lg','skt']

for word in replace_word:
    lower_text.replace(word,'**')
print(lower_text)






# 모든 문자를 소문자로 변환
text = text.lower()
text = text.split()
for i in text:
    if (i == 'kt') or (i == 'skt') or (i == 'samsung') or (i == 'lg'):
        for j in range(len(text)):
            if i == text[j]:
                text[j] = "**"
print(" ".join(text))