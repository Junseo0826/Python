'''
    작성일 : 2023년 11월 8일
    작성자 : 컴퓨터공학부 202395025 이준서
    설명 : 심화문제 8-6
'''
student_tuple = [
    ('211101', '강이안', '010-123-1111'),
    ('211102', '박동민', '010-123-2222'),
    ('211103', '김수정', '010-123-3333')   
]
student_dict = {}
for id_num, name, phone in student_tuple:
    student_dict[id_num] = name,phone

for key, value in student_dict.items():
    print(key,":", value[1])
    
id = input("학번을 입력하세요 : ")
print(f"{id} 학생은 {student_dict[id][0]}이며, 전화번호는 {student_dict[id][1]}입니다.")