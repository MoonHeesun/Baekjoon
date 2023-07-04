N = int(input())

for i in range(0,N):
    print(" "*(N-(i+1)), "*"*(2*i+1),sep="")

for j in range(1,N):
    print(" "*j, "*"*(2*N-(2*j+1)),sep="")