# 문제: 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램
# 입력: 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수
# 출력: 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력

#import sys
#List = list(map(int, sys.stdin.readline().split()))
#max = List[0]
#location = 1
#for i in range(9):
    #if max < List[i]:
        #max = List[i]
        #location = location + 1
#print(max)
#print(location)
# ⬆ 코딩은 9개의 정수를 입력받는 조건에 부합하지 않아서 틀린 것이다.

List = []
max = 0

# 정수 9개 입력
for i in range(9):
    num = int(input())
    List.append(num)

# 최대값과 위치
for i in range(9):
    if max < List[i]:
        max = List[i]
        location = i + 1
print(max)
print(location)