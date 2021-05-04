#문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력
#입력: 첫째 줄에 테스트 케이스의 개수 T (0<A, B<10)
#출력: 각 테스트 케이스마다 A+B를 출력

#연산문
T = int(input("테스트 케이스 횟수: "))
for i in range (T):
    A, B = map(int, input().split())
    sum = A+B

#출력문 - 파이썬은 출력문을 따로 써줘야 함
for i in range (T):
        print(sum)
