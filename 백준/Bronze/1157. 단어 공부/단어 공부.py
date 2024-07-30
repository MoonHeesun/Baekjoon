word = input().upper()

word_lst = {}
for w in word:
    if w not in word_lst:
        word_lst[w] = 0
    word_lst[w] += 1

max_cnt = -1
for key in word_lst:
    if max_cnt < word_lst[key]:
        max_cnt = word_lst[key]
        max_char = key

if list(word_lst.values()).count(max_cnt) == 1:
    print(max_char)
else:
    print("?")