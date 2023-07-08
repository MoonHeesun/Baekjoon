# 일곱 난쟁이
height_sum = 0
height_list = []

for i in range(9):
    height = int(input())
    height_sum = height_sum + height
    height_list.append(height)
height_list.sort()

is_ok = False
for first in height_list:
    for second in height_list:
        if first == second:
            continue
        if (height_sum - (first+second)) == 100:
            height_list.remove(second)  # 앞에거부터 지우면 리스트가 밀리면서 문제 생김
            height_list.remove(first)
            is_ok = True 
# 리스트 중 삭제를 했으니 에러뜸. 찾았으면 튀어나오도록 하면 됨
        if is_ok:
            break
    if is_ok:
        break
        
for i in range(len(height_list)):
    print(height_list[i])