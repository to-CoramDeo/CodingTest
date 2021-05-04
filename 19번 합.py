#문제: n이 주어졌을 때, 1부터 n까지 합
#입력: 첫째 줄에 n (1 ≤ n ≤ 10,000)
#출력: 1부터 n까지 합

#변수 선언
num = 1
sum = 0

#연산문
n = int(input())
for i in range(n):
    sum = sum + num
    num = num + 1
print(sum)