f = open("q1-input.txt","r")
q = int(f.readline())
args = f.readlines()
for i in range(len(args)):
    args[i] = int(args[i])
k = [2]
i = 2
while len(k) <= max(args):
    i+=1
    flag = 1
    for n in range(2,int(i**0.5)+1):
        if (i%n == 0):
            flag = 0
    if flag == 0:
        continue
    if abs(i-k[-1]) == 2:
        k.append(i)
        k.append(i)
    else:
        k.append(i)
        
for el in args:
    print(k[el-1])