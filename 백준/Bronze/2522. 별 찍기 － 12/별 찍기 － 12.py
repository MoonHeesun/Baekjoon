N = int(input())

for i in range(0,N):
    print(" "*(N-(i+1)), "*"*(i+1), sep="")

for j in range(1,N):
    print(" "*j, "*"*(N-j), sep="")