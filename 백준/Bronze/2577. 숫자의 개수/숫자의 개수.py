a = int(input())
b = int(input())
c = int(input())
result = str(a*b*c)

result_lst = []
for i in result:
    result_lst.append(int(i))

for num in range(0,10):
    print(result_lst.count(num))