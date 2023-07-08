## 방식 1

h, m = map(int, input().split())
t = int(input())
if m+t < 60:
    print(h,m+t)
else:
    if h+((m+t)//60) < 24:
        print(h+((m+t)//60), ((m+t)%60))
    else:
        print(((h+((m+t)//60)))-24, ((m+t)%60))

## 방식 2

# h, m = map(int, input().split())
# t = int(input())
        
# final_m = h * 60 + m + t
# final_h = (final_m // 60) % 24
# final_m = final_m % 60
# print(final_h, final_m)
