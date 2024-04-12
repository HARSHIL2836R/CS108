f = open("q2-input.txt","r")
sets = f.readlines()
f.close()
for i in range(len(sets)):
    if i == 0:
        l = sets[i].strip().split(',')
        continue
    for el in sets[i].strip().split(','):
        if el in l:
            continue
        else:
            l.append(el)
print(l)