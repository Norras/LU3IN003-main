from typing import Tuple
from DIST_1 import DIST_1
from SOL_1 import SOL_1
from GetTab_Dist1 import Tab_DIST_1

def PROG_DYN(x:list[str],y:list[str])->Tuple[int,Tuple[list[str],list[str]]]:
    dist = DIST_1(x,y)
    return (dist,SOL_1(x,y,Tab_DIST_1(x,y)))
