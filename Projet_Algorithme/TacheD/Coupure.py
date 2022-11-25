import math
from GetTab_Dist1 import Tab_DIST_1

c_del:int=2
c_ins:int=2
c_sub:int=4
c_sub_conc:int=3

def coupure(x,y):
    tab = []
    I = []
    i_prim = math.floor(len(x)/2)

    # #INITIALISATION DE D
    for i in range(2):
        line = []
        for j in range(len(y)+1):
            line.append(0)
        tab.append(line)

    for j in range(len(y)+1):
        tab[0][j] = j*c_ins
    #INITIALISATION DE I
    for i in range(2):
        line = []
        for j in range(len(y)+1):
            line.append(0)
        I.append(line)
    
    # ON AVANCE LES VALEURS DE D JUSQU'A i_prim
    for i in range(1,i_prim):
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


    for i in range(i_prim,len(x)+1):
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
            if(i == i_prim):
                I[1][j] = j
            elif(tab[1][j] == deletion):
                I[1][j] = I[0][j]
            elif(tab[1][j] == insertion):
                I[1][j] = I[1][j-1]
            elif(tab[1][j] == substitution):
                I[1][j] = I[0][j-1]
        #AFFICHAGE DU TABLEAU I
        #print("Tableau de coupure")
        #for dist in I:
        #    print(dist)

        #REMPLACE LES VALEURS DE LA LIGNE D'INDICE 0 PAR CEUX DE LA LIGNE D'INDICE 1
        for k in range(len(y)+1):
            tab[0][k] = tab[1][k]
            I[0][k] = I[1][k]
    
    return I[0][len(y)]

