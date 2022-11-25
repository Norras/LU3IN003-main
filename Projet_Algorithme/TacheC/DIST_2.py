c_del:int=2
c_ins:int=2
c_sub:int=4
c_sub_conc:int=3

def DIST_2(x:list[str],y:list[str])->int:
    tab = []
    #INITIALISATION 
    for i in range(2):
        line = []
        for j in range(len(y)+1):
            line.append(0)
        tab.append(line)

    #INITIALISATION 1ERE LIGNE DU TABLEAU
    for j in range(len(y)+1):
        tab[0][j] = j*c_ins
        
    for i in range(1,len(x)+1):
        tab[1][0] = i*c_del
        for j in range(1, len(y)+1):
            deletion = tab[0][j]+c_del
            insertion = tab[1][j-1]+c_ins
            substitution:int
            if(x[i-1] == y[j-1]):
                substitution = tab[0][j-1]
            elif (({x[i-1],y[j-1]}=={'A','T'}) or ({x[i-1],y[j-1]}=={'G','C'})):
                substitution = tab[0][j-1]+c_sub_conc
            else:
                substitution = tab[0][j-1]+c_sub
            tab[1][j] = min(deletion, insertion, substitution)
        
        #REMPLACE LES VALEURS DE LA LIGNE D'INDICE 0 PAR CEUX DE LA LIGNE D'INDICE 1
        for k in range(len(y)+1):
            tab[0][k] = tab[1][k]

    #AFFICHAGE DU TABLEAU 
    #for dist in tab:
    #    print(dist)
    
    return tab[0][len(y)]