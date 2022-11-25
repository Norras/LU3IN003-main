import sys 


c_del:int=2
c_ins:int=2
c_sub:int=4
c_sub_conc:int=3


## Fonctions ##
def DIST_NAIF_REC(x:list[str],y:list[str],i:int,j:int,c:int,dist:int)->int:
    modx:int=len(x)-1
    mody:int=len(y)-1
    if (i==modx and j==mody):
        if (c<dist):
            dist=c
    else:
        if (i<modx and j<mody):
            if (x[i]==y[j]):  # Truc étrange : on nous dit c_(x_i+1,y_j+1) mais du coup si y'a une sub à i,j=0 ca le saute
                dist=DIST_NAIF_REC(x,y,i+1,j+1,c,dist)
            elif (({x[i],y[j]}=={'A','T'}) or ({x[i],y[j]}=={'G','C'})):
                dist=DIST_NAIF_REC(x,y,i+1,j+1,c+c_sub_conc,dist)
            else:   
                dist=DIST_NAIF_REC(x,y,i+1,j+1,c+c_sub,dist)
        
        if (i<modx):
            dist=DIST_NAIF_REC(x,y,i+1,j,c+c_del,dist)
        if (j<mody):
            dist=DIST_NAIF_REC(x,y,i,j+1,c+c_ins,dist)
    return dist

def DIST_NAIF(x:list[str],y:list[str])->int:
    return DIST_NAIF_REC(x,y,0,0,0,sys.maxsize)





# Tests

## Traitement du fichier Inst_0000010_44.adn ##
file=open("./Instances_genome/Inst_0000010_44.adn")
modx:int=int(file.readline())
mody:int=int(file.readline())
x:list[str]=file.readline().split(" ")
y:list[str]=file.readline().split(" ")
file.close()
x=x[:-1]
y=y[:-1]

print("Mot x :%s"%(x))
print("Mot y :%s"%(y))
print("Distance d'édition : %d"%(DIST_NAIF(x,y)))
print("----------------------")

## Traitement du fichier Inst_0000010_7.adn ##
file=open("./Instances_genome/Inst_0000010_7.adn")
modx:int=int(file.readline())
mody:int=int(file.readline())
x:list[str]=file.readline().split(" ")
y:list[str]=file.readline().split(" ")
file.close()
x=x[:-1]
y=y[:-1]
print("Mot x :%s"%(x))
print("Mot y :%s"%(y))
print("Distance d'édition : %d"%(DIST_NAIF(x,y)))
print("----------------------")

## Traitement du fichier Inst_0000010_8.adn ##
file=open("./Instances_genome/Inst_0000010_8.adn")
modx:int=int(file.readline())
mody:int=int(file.readline())
x:list[str]=file.readline().split(" ")
y:list[str]=file.readline().split(" ")
file.close()
x=x[:-1]
y=y[:-1]
print("Mot x :%s"%(x))
print("Mot y :%s"%(y))
print("Distance d'édition : %d"%(DIST_NAIF(x,y)))
print("----------------------")




