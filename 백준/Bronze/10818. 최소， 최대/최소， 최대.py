N = int(input())
r = list(map(int, input().split()))
R = sorted(r)
print(R[0], R[N-1])