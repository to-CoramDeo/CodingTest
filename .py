# 변수 설정
N, X = map(int, input().split()) # int()의 인자에 '리스트'는 올 수 없다.
A = input().split()
B = []

for i in range(N):
    if int(A[i]) < X:
        B.append(int(A[i]))
print(B)
