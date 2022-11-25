import math
from Coupure import coupure
from mot_gaps import mot_gaps
from align import align_lettre_mot

def SOL_2(x,y):
    if(len(y) == 0 and len(x) > 0):
        return (x, mot_gaps(len(x)))
    if(len(x) == 0 and len(y) > 0):
        return (mot_gaps(len(y)), y)
    if(len(x) ==  1 and len(y) == 1):
        return (x,y)
    if(len(x) == 1 and len(y) > 1):
        return (align_lettre_mot(x,y),y)
    
    i = math.floor(len(x)/2)
    j = coupure(x,y)
    #print("i : %d"%i)
    #print("j : %d"%j)
    u = SOL_2(x[:i],y[:j])
    v = SOL_2(x[i:],y[j:])
    #print(u)
    #print(v)
    return (u[0]+v[0], u[1]+v[1])