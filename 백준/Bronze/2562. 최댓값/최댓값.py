num_lst = [int(input()) for i in range(9)]
max_num = max(num_lst)
order = num_lst.index(max_num) + 1

print(max_num)
print(order)