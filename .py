N = 26 # N[1]
print(N//10) # 몫: 2
print(N%10) # 나머지: 6
SUM = (N//10)+(N%10) # 몫 + 나머지: 8
N = str(N%10) + str(SUM) # N[2]: 6 8

print(SUM) # 8
print(N) # 14 -> 6 8 
/