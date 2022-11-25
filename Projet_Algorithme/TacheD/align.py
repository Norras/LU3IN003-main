from mot_gaps import mot_gaps

def align_lettre_mot(x,y):
    for i in range(len(y)):
        if(y[i] == x) or ({x,y[i]}=={'A','T'}) or ({x,y[i]}=={'G','C'}):
            return mot_gaps(i-1)+x+mot_gaps(len(y)-i-1)
    return mot_gaps(len(y))+x
