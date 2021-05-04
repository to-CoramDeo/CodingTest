#문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력
#입력: 첫째 줄에 테스트 케이스의 개수 T (0<A, B<10)
#출력: 각 테스트 케이스마다 A+B를 출력

T = int(input())
for i in range (T):
    A, B = map(int, input().split())
    print(A+B)