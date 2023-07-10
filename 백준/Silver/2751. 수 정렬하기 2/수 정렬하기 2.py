# 수 정렬하기2 - 입력 횟수가 많아지면 빠른 입출력 필요 ---> sys.stdin.readline() 이용
import sys
N = int(sys.stdin.readline())
num_list = []

for i in range(N):
    num_list.append(int(sys.stdin.readline()))

num_list = sorted(num_list)
for i in num_list:
    print(i)