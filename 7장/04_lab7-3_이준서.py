'''
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터공학부 202395025 이준서
    설명 : 도시의 인구 자료에 대한 슬라이싱하기.
'''
population = ['Seoul',9765,'Busan',3441,'Incheon',2954]
print("서울 인구 : ", population[1])        # 리스트의 두번째 요소 출력
print("인천 인구 : ", population[-2])       # 리스트의 -2번째 요소 출력
print("도시 리스트 : ",population[::2])     # 스텝값을 2로하여 도시 리스트 출력
print("인구 : ",population[1::2])          # 스텝값을 2로하여 인구 리스트 출력
print("인구의 합 : ",sum(population[1::2])) # 스텝값을 2로하여 인구 수의 총합을 출력