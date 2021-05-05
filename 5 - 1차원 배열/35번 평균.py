# 문제: 점수 중 최대값을 M이라고 하자. 모든 점수를 점수/M*100으로 고쳤다. 고친 점수의 평균을 구해라.
# 입력: 첫째 줄에 시험 본 과목의 개수 N, 둘째 줄에 현재 성적
# 출력: 첫째 줄에 새로운 평균을 출력

N = int(input())
M = 0
score = list(map(int, input().split()))

# 최대값 구하기
for i in range(N):
    if M < score[i]:
        M = score[i]
print(M)


# ⬇ JT 형님이랑 알고리즘 이야기를 나눔
# average = (sum(score)/M*100)/N
# print(average)
# -> 수학 연산을 간결하게 작성하는 편인 것 같음 