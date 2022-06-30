line = '0123456789ABCDEF'
def haiSangMuoi(n):
    p = 0
    dec = 0
    i = len(n)-1
    while i>=0:
        dec += int(n[i]) * pow(2, p)
        p +=1
        i -=1
    return dec
t = int(input())
while t!=0:
    b = int(input())
    n = input()
    c = haiSangMuoi(n)
    
    res = []
    while(c != 0):
        res.append( c%b )
        c //= b
    # print(res)
    res.reverse()
    for i in res:
        print(line[ int(i) ], sep = '',end='')
    print('')
    t -= 1