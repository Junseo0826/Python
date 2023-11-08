'''
    작성일 : 2023년 11월 8일
    작성자 : 컴퓨터공학부 202395025 이준서
    설명 : LAB 8-3 파티 동시 참석자 알아내기
'''
partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])

print("파티 A, B에 모두 참석한 사람들 : ", partyA.intersection(partyB))
print("파티 A, B에 참석한 사람들 : ", partyA.union(partyB))
print("파티 A, B에 중복없이 참석한 사람들 : ", partyA.symmetric_difference(partyB))
print("파티 A에만 참석한 사람들 : ", partyA.difference(partyB))