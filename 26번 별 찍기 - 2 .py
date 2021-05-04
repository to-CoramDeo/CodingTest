# 문제: 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제 (오른쪽 정렬)
# 입력: 첫째 줄에 N(1 ≤ N ≤ 100)
# 출력: 첫째 줄부터 N번째 줄까지 차례대로 별을 출력

N = int(input()) # 입력 값이 1개 일때는 input()을 써주는 게 좋다.
star = "*"
space = " "

for i in range(N):
    i = i+1
    print(space*(N-i) + star*i) 

# 좋은 코드인지 잘 모르겠다. 정렬 칸을 정해주고 싶다.