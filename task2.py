N={'1':[0,0],'2':[0,0],'3':[0,0]} # 0 - кол-вщ груза 1- объём

with open ('travels.txt' , 'r') as f:
    for i in f:
        L=i.split
        if i[0] == 1:
            N['1'][0]+=1
            N['1'][1]+=int(L[6])
        elif i[0] == 2:
            N['2'][0]+=1
            N['2'][1]+=int(L[6])
        else:
            N['3'][0]+=1
            N['3'][1]+=int(L[6])
print(N)