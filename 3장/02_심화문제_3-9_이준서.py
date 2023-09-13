'''
    작성일 : 2023년 09월 13일
    작성자 : 컴퓨터공학부 202395025 이준서
    설명 : 90페이지 문제 3.9
            평균 시속과 이동시간을 입력받아.
            이동 시간은 시, 분, 초 단위로 출력하고,
            이동한 거리를 계산하여 출력하시오.
'''
# 1. 시속 입력 받기
speed = float(input('평균 시속(km/h)을 입력하세요 : '))
# 2. 시간 입력 받기
time = float(input('이동 시간(h)을 입력하세요 : '))
# 3. 계산
total_time = time * 3600
hour = total_time // 3600
min = (total_time % 3600) // 60
sec = total_time % 60
# 4. 시속, 시간, 거리 출력
print('평균 시속 : {}(km/h)'.format(speed))
print('이동 시간 : {:.0f}시간 {:.0f}분 {:.0f}초'.format(hour,min,sec))
print('이동 거리 : ', speed * time,'km')