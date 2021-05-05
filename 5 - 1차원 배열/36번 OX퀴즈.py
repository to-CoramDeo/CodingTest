# 문제: "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다. OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램
# 입력: 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.
# 출력: 각 테스트 케이스마다 점수를 출력

TestCase = int(input())

score = 0 
scoreList = []
for i in range(TestCase):
    OX = list(input()) # 결과를 리스트로 받는다.
    for i in range(len(OX)): # 반복 범위로 len(리스트) 가능하다.
        if OX[i] == "O":
            score = score + 1
            scoreList.append(score)
        elif OX[i] == "X":
            score = 0
    score = 0
    print(sum(scoreList))
    scoreList.clear() # 리스트 내부의 요소를 모두 제거합니다.


# ⬇ 아래의 코드는 EOF 오류가 떴습니다. # EOF: 프로그램이 예상치 못하게 끝났다.
# TestCase = int(input())
# score = 0 
# scoreList = []
# while True:
#     OX = list(input()) # 결과를 리스트로 받는다.
#     for i in range(len(OX)):
#         if OX[i] == "O":
#             score = score + 1
#             scoreList.append(score)
#         elif OX[i] == "X":
#             score = 0
#     score = 0
#     print(sum(scoreList))
#     scoreList.clear() # 리스트 내부의 요소를 모두 제거합니다.
# 예상해보자면 while True: 반복문의 종결을 구현하지 않았습니다. 
