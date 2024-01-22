n=0
with open ('Perepis.txt' , 'r') as f:
    for i in f:
        L = i.split()
        s=L[3]
        if int( s[6::] ) <= 1978:
            print(L[0])
            n+=1
print('Всего людей родившихся раньше 1978 годa =', n)