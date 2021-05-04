# 문제: 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력
# 입력: 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000) 둘째 줄에 수열 A를 이루는 정수 N개 
# 출력: X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력

N, X = map(int, input().split()) # int()의 인자에 '리스트'는 올 수 없다.
A = input().split()

for i in range(N):
    if int(A[i]) < X:
        print(int(A[i]), end=" ") # end=" "를 이용하여 한 줄에 출력한다.