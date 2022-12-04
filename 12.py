i_str = 'abacabaabc'
#i_str = input()

max_substr_l = int(len(i_str)/2)
i_str_l = int(len(i_str))
positions = len(i_str)-max_substr_l+1

s_strs = []
s_count = []
s_endswith = []
s_predictable = []
for j in range(0, max_substr_l-1):
    calc_max_substr_l = max_substr_l - j
    calc_positions = len(i_str)-calc_max_substr_l+1
    for i in range(0, calc_positions):
        s_str = i_str[i:i+calc_max_substr_l]
        if s_str in s_strs:
            s_count.append(-1)
            s_strs.append('found')
            s_predictable.append(-1)
            s_count[s_strs.index(s_str)] += 1

            endswith = i_str[i+calc_max_substr_l:i+calc_max_substr_l+1]

            if endswith != s_endswith[s_strs.index(s_str)]:
                s_predictable[s_strs.index(s_str)] = 0

            if i+calc_max_substr_l == i_str_l:
                s_endswith.append('\r')
            else:
                s_endswith.append(endswith)
        else:
            s_predictable.append(1)
            if i+calc_max_substr_l == i_str_l:
                s_endswith.append('\r')
            else:
                s_endswith.append(i_str[i+calc_max_substr_l:i+calc_max_substr_l+1])
            s_count.append(1)
            s_strs.append(s_str)

    if 0 in s_predictable:
        break

idx = s_predictable.index(0)
print(len(s_strs[idx]))

print(s_strs)
print(s_count)
print(s_endswith)
print(s_predictable)
