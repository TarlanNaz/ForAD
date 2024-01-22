ot=int(input())
do=int(input())
with open ('Perepis.txt' , 'r') as f:
    for i in f:
        L = i.split()
        s=L[3]
        if ot <= int( s[6::] ) <= do:
            print(i)
