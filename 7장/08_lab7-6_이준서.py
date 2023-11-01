'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 202395025 이준서
    설명 : LAB 7-6 도시의 이름과 인구를 튜플로 묶어보자.
'''
# 다음과 같은 리스트가 생성되어 있다.
city_info = [('서울', 9765), ('부산', 3441), ('인천', 2954), ('광주', 1501), ('대전', 1531)]

max_pop = 0                 # max_pop에 0을 넣는다 (city_info에 있는 값들보다 작은 값을 넣어 max_city에 city_info에 있는 변수들을 저장하기 위해)
min_pop = 9999              # min_pop에는 999999와 같이 매우 큰 값을 넣는다. (city_info에 있는 값들보다 큰 값을 넣어 min_city에 city_info에 있는 변수들을 저장하기 위해)
total_pop = 0               # total_pop에는 0을 저장한다.

max_city = None             # max_city에 빈 값을 저장한다.
min_city = None             # min_city에 빈 값을 저장한다.

for city in city_info:      # city_info에 있는 변수들을 가져와 반복하면서
    total_pop += city[1]    # city의 1번지 값을 total_pop에 복합연산자를 통해 저장한다.
    if city[1] > max_pop :  # 만약 city의 1번지 값이 max_pop보다 크다면
        max_pop = city[1]   # max_pop에 city의 1번지 값을 저장한다.
        max_city = city     # max_city에 city를 저장한다.
    if city[1] < min_pop :  # 만약 city의 1번지 값이 min_pop보다 작다면
        min_pop = city[1]   # min_pop에 city의 1번지 값을 저장한다.
        min_city = city     # min_city에 city를 저장한다.
# 출력
print("최대인구 : {0}, 인구 : {1} 천명".format(max_city[0], max_city[1]))
print("최소인구 : {0}, 인구 : {1} 천명".format(min_city[0], min_city[1]))
print("리스트 도시 평균 인구 : {0} 천명".format(total_pop / len(city_info)))