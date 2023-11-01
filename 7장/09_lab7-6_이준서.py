'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 202395025 이준서
    설명 : LAB 7-6 도시의 이름과 인구를 튜플로 묶어보자.
'''
# 다음과 같은 리스트가 생성되어 있다.
city_info = [('서울', 9765), ('부산', 3441), ('인천', 2954), ('광주', 1501), ('대전', 1531)]

max_population = city_info[0][1]   # 첫번째 항목이 기준
min_population = city_info[0][1]
total_pop = 0

max_city = city_info[0][0]  # 첫번째 항목이 기준
min_city = city_info[0][0]

for city, population in city_info:
    total_pop += population 
    if population > max_population :
        max_population = population
        max_city = city
    if population < min_population :
        min_population = population
        min_city = city
# 출력
print("최대인구 : {0}, 인구 : {1} 천명".format(max_city, max_population))
print("최소인구 : {0}, 인구 : {1} 천명".format(min_city, min_population))
print("리스트 도시 평균 인구 : {0} 천명".format(total_pop / len(city_info)))