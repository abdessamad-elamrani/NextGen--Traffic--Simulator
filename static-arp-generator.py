# finale result should be 4001


f = open("DUT-StaticARP.txt", "w")
ind = 1
i = 0
j = 2
for ind in range(1,40000):
    f.write('''
        edit {}
        set interface "port6"
        set ip 1.1.{}.{} 
        set mac 11:11:11:11:11:11
        next'''.format(ind, i, j))
    j += 1
    if j == 255:
        j = 1
        i += 1
    ind += 1

f.write('end')

f.close()


