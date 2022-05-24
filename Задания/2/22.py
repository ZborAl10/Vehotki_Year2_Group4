f = open('22.txt', 'r+')
nf = open('22n.txt','w')

far = f.readlines()

for i in range(len(far)):
    fl = False
    tstr = ''
    
    if far[i][-1] == '\n':
        ar = list(map(int,far[i][:-1].split()))
        fl = True
    else:
        ar = list(map(int,far[i].split()))

    c = ar[0]

    for j in range(1,len(ar)):
        
        if c == 0:
            chrc = 0
        else:
            chrc = c/abs(c)
            
        if ar[j] == 0:
            chraj = 0
        else:
            chraj = ar[j]/abs(ar[j])
        
        if chrc == chraj:
            c += ar[j]
        else:
            tstr += str(c)
            tstr += ' '
            c = ar[j]
            
    tstr += str(c)

    if fl:
        tstr += '\n'
        
    nf.write(str(tstr))
    
f.close()
nf.close()
    
