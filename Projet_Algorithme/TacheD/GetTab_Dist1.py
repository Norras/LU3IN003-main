
c_del:int=2
c_ins:int=2
c_sub:int=4
c_sub_conc:int=3

def Tab_DIST_1(x:list[str],y:list[str]):
    tab = []
    for i in range(len(x)+1):
        line = []
        for j in range(len(y)+1):
            line.append(0)
        tab.append(line)

    for i in range(len(x)+1):
        tab[i][0] = i*c_del
    for j in range(len(y)+1):
        tab[0][j] = j*c_ins
    
    for i in range(1,len(x)+1):
        for j in range(1, len(y)+1):
            deletion = tab[i-1][j]+c_del
            insertion = tab[i][j-1]+c_ins
            substitution:int
            if(x[i-1] == y[j-1]):
                substitution = tab[i-1][j-1]
            elif (({x[i-1],y[j-1]}=={'A','T'}) or ({x[i-1],y[j-1]}=={'G','C'})):
                substitution = tab[i-1][j-1]+c_sub_conc
            else:
                substitution = tab[i-1][j-1]+c_sub
            tab[i][j] = min(deletion, insertion, substitution)


    #AFFICHAGE DU TABLEAU
    #for dist in tab:
    #    print(dist)

    return tab
