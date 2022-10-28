x = int(input("сколько переменных\n"))
t = []
print("введи последовательность значений функции")
for i in range(2**x):
    t.append(int(input('-> ')))

resSDNF = ''
resSKNF = ''
for i in range(2**x):
    s = bin(i)[2:]
    while len(s) != x:
        s = '0'+ s
    
    if t[i] == 1:
        resSDNF += '('
    else:
        resSKNF += '('
    for j in range(x):
        a = 'xyz'
        if t[i] == 1:
            if s[j] == '0':
                resSDNF += '!'+a[j]+' * '
            else:
                resSDNF += a[j]+' * '
        else:
            if s[j] == '0':
                resSKNF += a[j]+' + '
            else:
                resSKNF += '!'+a[j]+' + '
    
    if t[i] == 1:
        resSDNF = resSDNF[:-3]+') + '
    else:
        resSKNF = resSKNF[:-3]+') * '
       
print(f'SDNF : {resSDNF[:-3]}')
print(f'SKNF : {resSKNF[:-3]}')

