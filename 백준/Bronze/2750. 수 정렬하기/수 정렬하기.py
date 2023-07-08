# 수 정렬하기1
n = int(input())

arr = []
for i in range(n):
    num = int(input())
    arr.append(num)

for i in range(n-1):
    min_idx = i
    for j in range(i+1, n):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

for i in arr:
    print(i)