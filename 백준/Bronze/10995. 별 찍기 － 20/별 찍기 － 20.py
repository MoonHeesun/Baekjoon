n = int(input())
a = 1

for i in range(n):
    if a%2 != 0:
        print('* '*n, sep='')
        a += 1
    else:
        print(' *'*n, sep='')
        a += 1