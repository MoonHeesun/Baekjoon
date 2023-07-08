N = int(input())

for i in range(0,N):
    print("*"*(i+1), " "*(2*N-2*(i+1)), "*"*(i+1), sep="")

for i in range(1,N):
    print("*"*(N-i), " "*2*i, "*"*(N-i), sep="")

# 절댓값 이용 방식
# n = int(input())
# for i in range(1, 2*n):
#   col = 2 * n
#   star = (n - abs(n-i))   # abs(): 절댓값 함수
#   l = '*' * star + ' ' * (col - 2*star) + '*' * star
#   print(l)
