# 문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력
# 입력: 첫째 줄에 테스트 케이스의 개수 T가 주어진다, 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력: 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
import sys
T = int(sys.stdin.readline()) # input()보다 1) 빠름 2) 사용자가 느리게 입력해도 오류가 안 남

for i in range (T):
    A, B = map(int, sys.stdin.readline().split())
    i = i+1
    print("Case #%s: %s + %s = %s" %(i, A, B, A+B))