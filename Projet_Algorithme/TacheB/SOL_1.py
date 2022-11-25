from http.client import USE_PROXY
from operator import index
from typing import Tuple

c_del:int=2
c_ins:int=2
c_sub:int=4
c_sub_conc:int=3

def SOL_1(x:list[str],y:list[str],t:list[int])->Tuple[list[str],list[str]]:
    u:list[str]=[]
    v:list[str]=[]
    index1 = len(x)
    index2 = len(y)

    while(index1 > 0 or index2 > 0):
        dist = t[index1][index2]
        deletion = t[index1-1][index2]
        insertion = t[index1][index2-1]
        substitution = t[index1-1][index2-1]

        if(deletion+c_del == dist):
            u+=x[index1-1]
            v+='-'
            index1 = index1-1
        elif(insertion+c_ins == dist):
            u+='-'
            v+=y[index2-1]
            index2 = index2-1
        elif(substitution == dist or substitution+c_sub_conc == dist or substitution+c_sub == dist):
            u+=x[index1-1]
            v+=y[index2-1]
            index1 = index1-1
            index2 = index2-1

    u_x = ''
    v_y = ''

    for i in u:
        u_x = i + u_x
    for j in v:
        v_y = j + v_y

    return(u_x, v_y)
