import sys

lst = [num for num in range(1, 31)]
n_lst = sorted([int(sys.stdin.readline()) for _ in range(28)])

answer_lst = []
for num in lst:
    if num not in n_lst:
        answer_lst.append(num)

for i in answer_lst:
    print(i)