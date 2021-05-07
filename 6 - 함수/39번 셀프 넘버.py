# 문제: 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수
# 입력: 없음
# 출력: 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력

# ⬇⬇ 틀린 코드다. 이유는 모르겠네.......U__U
# def SelfNumber():
#     for n in range(1, 15): # 양의 정수 1부터 10,000까지 반복한다.
#         for nn in str(n): # i가 10이라면, "1", "0" 두 번 반복합니다.
#             nn = nn + n
#             print(nn)
# SelfNumber()

# dn = n + for i in str(n)


# dn = n + n의 각 자리수
dn = []
for n in range(1, 10001): # 15
    for i in str(n): # '1', '5'
        n = n + int(i) # 15 + 1 + 5
    dn.append(n)

# 셀프 넘버는 {범위의 수} - {dn}         # {}: 집합
self_number = sorted(set(range(1, 10001))-set(dn)) # set(): 중복을 제거합니다.
for i in self_number:
    print(i)

# -> 함수를 이용해서 푼건지 모르겠다. 아직은 함수가 익숙하지 않다.