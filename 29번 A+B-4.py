# 문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력
# 입력: 입력은 여러 개의 테스트 케이스로 이루어졌다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력: 각 테스트 케이스마다 A+B를 출력

while True:
    try: # 예외 처리 구문
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
