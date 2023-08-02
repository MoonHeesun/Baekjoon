n = int(input())
t_list = []
p_list = []
for day in range(n):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

def fn(curr, total_pay):
    global answer
    if curr == n:
        answer = max(total_pay, answer)
        return
    if (curr+t_list[curr]) <= n:
        fn(curr+t_list[curr], total_pay+p_list[curr])
    fn(curr+1, total_pay)

answer = 0
res = []
for i in range(n):
    fn(i, 0)
print(answer)