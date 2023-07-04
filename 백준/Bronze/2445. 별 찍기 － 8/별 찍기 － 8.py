N = int(input())

for i in range(0,N):
    print("*"*(i+1), " "*(2*N-2*(i+1)), "*"*(i+1), sep="")

for i in range(1,N):
    print("*"*(N-i), " "*2*i, "*"*(N-i), sep="")