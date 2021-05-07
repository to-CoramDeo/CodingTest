N = int(input())

for i in range(N):
    if N > 5:
        N = N -5
    else:
        if N%3 == 0:
            print("ok")
        else: 
            print("no")
print(N)