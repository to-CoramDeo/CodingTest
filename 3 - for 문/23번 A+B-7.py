# 문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력
# 입력: 첫째 줄에 테스트 케이스의 개수 T, 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력: 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

T = int(input())

for i in range(T):
    A,B = map(int, input().split())
    i = i+1
    print("Case #%s: %s" %(i, A+B))

# 아래의 결과는 틀렸다고 하는데 이유는 모름!! 백준씌 까다로우시넹 :)
# T = int(input())
# for i in range(T):
#     A,B = map(int, input().split())
#     i = i+1
#     print("Case #",i,": ",A+B)