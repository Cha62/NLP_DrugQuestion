f = open("CIS_bdpm.txt")
g = open('drug_list.txt','w')
name_prec = ''
for line in f:
    i = 9
    name = ''
    
    while line[i] != ' ' and line[i] != ',':
        name += line[i]
        
        i+=1
    if name != name_prec:
        g.write(name+'\n')
    name_prec = name