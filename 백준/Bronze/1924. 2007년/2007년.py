x, y = map(int, input().split())
t = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

if x == 1:
    for i in range(0,7):
        if y%7 == i:
            print(day[i])
    else:
        pass
else:
    a = sum(t[:(x-1)]) + y
    for i in range(0,7):
        if a%7 == i:
            print(day[i])