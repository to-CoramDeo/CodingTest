

# 재귀함수로 풀기
def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N-1)
            
N = int(input())
print(factorial(N))