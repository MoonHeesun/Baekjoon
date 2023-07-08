num_list = []
for i in range(10):
    n = int(input())
    if n%42 in num_list:
        continue
    else:
        num_list.append(n%42)

print(len(num_list))