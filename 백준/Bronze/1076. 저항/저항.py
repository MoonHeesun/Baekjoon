col_list = ['black', 'brown', 'red', 'orange', 'yellow',
         'green', 'blue', 'violet', 'grey', 'white']
resis = []

for i in range(3):
    col = input()
    for j in range(len(col_list)):
        if col_list[j] == col:
            resis.append(j)

print((resis[0]*10+resis[1])*(10**resis[2]))