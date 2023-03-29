def rle(s):
    temp_list = []
    s += ' '
    letter = s[0]
    count_l = 1
    for i in range(1, len(s)):
        if s[i] == letter:
            count_l += 1
        else:
            if count_l == 1:
                temp_list.append(letter)
            else:
                temp_list.append(f'{letter}{count_l}')
                count_l = 1
            letter = s[i]
    return temp_list

x = rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')
print(*x, sep='')


def group_word(words):
    group = []
    new_dist = {}
    for word in words:
        sort_word = (''.join(sorted(word)))
        if not sort_word in new_dist.keys():
            new_dist[sort_word] = []
        new_dist[sort_word].append(word)
    for key, val in new_dist.items():
        group.append(val)
    print(group)


lists = ["eat", "tea", "tan", "ate", "nat", "bat","batt","tatb"]
group_word(lists)

