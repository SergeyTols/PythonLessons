s = 'сабака'
res = ''

for i in range(len(s)):
    if i == 1:
        res += 'о'
    else:
        res += s[i]

print(res)
