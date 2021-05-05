# 문제: 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
# 입력: 첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수
# 출력: 첫째 줄에 N의 사이클 길이를 출력

N = int(input()) 
origin = N
count = 0

while True:
    TensDigit = N//10
    UnitDigit = N%10 
    AddUnitandTensDigit = UnitDigit + TensDigit 
    N = int(str(UnitDigit) + str(AddUnitandTensDigit%10)) 
    count = count + 1
    if N == origin:
        break
print(count)