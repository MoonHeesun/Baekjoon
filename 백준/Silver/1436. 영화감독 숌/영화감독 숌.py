N = int(input())

num_list = []
for i in range(10000000):
    if '666' in str(i):
        num_list.append(i)
        if len(num_list) == N:
            print(num_list[N-1])