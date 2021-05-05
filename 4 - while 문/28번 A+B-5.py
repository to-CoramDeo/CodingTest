# 문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력
# 입력: 여러 개의 테스트 케이스, 각 테스트 케이스는 한 줄, 0<A.B<10, 마지막 입력에는 0이 두 개
# 출력: 각 테스트 케이스마다 A+B를 출력

while True:
    A, B = map(int, input().split())
    if A==0 and B==0:
        break
    else: 
        print(A+B)

# 오답 이유: A==0 and B==0이라고 합을 출력한다. 삐용
# while True:
#     A, B = map(int, input().split())
#     print(A+B)
#     if A == 0 and B == 0:
#         break