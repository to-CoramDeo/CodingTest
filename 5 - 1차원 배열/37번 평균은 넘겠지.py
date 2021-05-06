# 문제: 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
# 입력: 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
#       둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 출력: 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력

C = int(input())

for i in range(C): # C 만큼 반복한다.
    # 학생의 수, 학생들의 점수를 입력한다.
    N = list(map(int, input().split()))

    # 학생들 점수의 평균
    sum = 0
    for i in range(1, len(N)): # 1부터 N까지 반복한다.
        sum = sum + N[i]
    average = sum/N[0]
    
    # 평균을 넘는 학생 수
    count = 0
    for i in range(1, len(N)):   
        if average < N[i]:
            count = count+1

    percent = (count/N[0])*100
    print("{:.3f}%".format(percent)) # 소수점 아래 3자리만 출력한다.

# 코드를 보다 간결하게 작성하는 연습을 해야겠다.

#⬇ 같은 코드라고 생각하는데 백준은 틀렸다고 한다. 이유 아는 분!!?~~
# C = int(input())

# sum = 0
# count = 0
# for i in range(C): # C 만큼 반복한다.
#     # 학생의 수, 학생들의 점수를 입력한다.
#     N = list(map(int, input().split()))
#     for i in range(1, len(N)): # 1부터 N까지 반복한다.
#         sum = sum + N[i]
#     average = sum/N[0]
#     for i in range(1, len(N)):
#         if average < N[i]:
#             count = count+1
#     percent = (count/N[0])*100
#     print("{:.3f}%".format(percent))