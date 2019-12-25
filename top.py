f = open('top.txt', 'r',encoding='utf-8')

file = f.read()
file = file.split('\n')
top = ''

score = 0
top_s = 0
for i in range(len(file)):
    for j in range(i, len(file)):
        if file[i] == file[j]:
            score += 1
    if score > top_s:
        top_s = score
        top = file[i]
    score = 0
f.close()