N = int(input())

for i in range(0,N):
    print(" "*i, "*"*((2*N-1)-2*i), sep="")
    
for j in range(1,N):
    print(" "*(N-(j+1)), "*"*(2*j+1), sep="")