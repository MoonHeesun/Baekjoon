def get_max_revenue(current_day, total_pay):
    global answer

    # 마지막 날짜와 동일할 경우, 
    if current_day == n:
        answer = max(total_pay, answer)
        return
    if (current_day+t_lst[current_day]) <= n:
        get_max_revenue(current_day+t_lst[current_day], total_pay+p_lst[current_day])
    get_max_revenue(current_day+1, total_pay)

n = int(input())
t_lst = []
p_lst = []

for day in range(n):
    t, p = map(int, input().split())
    t_lst.append(t)
    p_lst.append(p)

answer = 0
res = []
for i in range(n):
    get_max_revenue(i, 0)
print(answer)