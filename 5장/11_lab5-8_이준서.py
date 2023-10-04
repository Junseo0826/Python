'''
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터공학부 202395025 이준서
    설명 : while문으로 별 그리기
            교재 131 페이지
'''
import turtle as t

t.shape("turtle")
i = 0
while i < 5:
    t.forward(100)
    t.right(144)
    t.forward(100)
    t.left(72)
    i += 1
t.mainloop()