l, c = map(int, input().split())
C = list(map(str, input().split()))
C.sort()
pw = [0 for _ in range(l)]
vow = ['a','e','i','o','u']

def fn(depth, idx):
    if depth == l:
        cnt_vow = 0
        for i in vow:
            if i in pw:
                cnt_vow += 1
        if cnt_vow >= 1 and (len(pw)-cnt_vow) >= 2:
            print(*pw, end='\n', sep='')
        return
    for j in range(idx, c):
        pw[depth] = C[j]
        fn(depth+1, j+1)

fn(0, 0)