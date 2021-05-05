#입력: 첫째 줄에 두 정수 H, M (0<=H<=23, 0<=M<=59)
#출력: 입력받은 시각 - 45분

H, M = map(int, input().split())

if M>=45:
    print(H, M-45)
elif M<45 and H>0:
    print(H-1, M+15)
else:
    print(H+23, M+15)

#JT's coding 
# h, m = map(int, input().split())
# if m < 45:
#     if h == 0:
#         h = 23
#     else:
#         h = h - 1
#     m = m + 15
# else:
#     m = m - 45

# print("%d %d" % (h, m))