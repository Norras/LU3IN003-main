from Coupure import coupure
from GetTab_Dist1 import Tab_DIST_1
from SOL_1 import SOL_1

# Tests
"""
## Traitement du fichier Inst_0000010_44.adn ##
file=open("../Instances_genome/Inst_0000010_44.adn")
modx:int=int(file.readline())
mody:int=int(file.readline())
x:list[str]=file.readline().split(" ")
y:list[str]=file.readline().split(" ")
file.close()
x=x[:-1]
y=y[:-1]

dist = Tab_DIST_1(x,y)
print("Distance d'édition")
for i in dist:
    print("" + str(i))

print("Mot x :%s"%(x))
print("Mot y :%s"%(y))
print("Un alignement de (x,y): ( %s , %s )"%(SOL_1(x,y,Tab_DIST_1(x,y))))
print("Coupure (x,y) : %d"%(coupure(x,y)))
print("----------------------")

## Traitement du fichier Inst_0000010_7.adn ##
file=open("../Instances_genome/Inst_0000010_7.adn")
modx:int=int(file.readline())
mody:int=int(file.readline())
x:list[str]=file.readline().split(" ")
y:list[str]=file.readline().split(" ")
file.close()
x=x[:-1]
y=y[:-1]

dist = Tab_DIST_1(x,y)
print("Distance d'édition")
for i in dist:
    print("" + str(i))

print("Mot x :%s"%(x))
print("Mot y :%s"%(y))
print("Un alignement de (x,y): ( %s , %s )"%(SOL_1(x,y,Tab_DIST_1(x,y))))
print("Coupure (x,y) : %d"%(coupure(x,y)))
print("----------------------")

## Traitement du fichier Inst_0000010_8.adn ##
file=open("../Instances_genome/Inst_0000010_8.adn")
modx:int=int(file.readline())
mody:int=int(file.readline())
x:list[str]=file.readline().split(" ")
y:list[str]=file.readline().split(" ")
file.close()
x=x[:-1]
y=y[:-1]

dist = Tab_DIST_1(x,y)
print("Distance d'édition")
for i in dist:
    print("" + str(i))

print("Mot x :%s"%(x))
print("Mot y :%s"%(y))
print("Un alignement de (x,y): ( %s , %s )"%(SOL_1(x,y,Tab_DIST_1(x,y))))
print("Coupure (x,y) : %d"%(coupure(x,y)))
print("----------------------")
"""
#Exemple
x ="ATTGTA"
y ="ATCTTA"

dist = Tab_DIST_1(x,y)
print("Distance d'édition")
for i in dist:
    print("" + str(i))

print("Mot x :%s"%(x))
print("Mot y :%s"%(y))
print("Un alignement de (x,y): ( %s , %s )"%(SOL_1(x,y,Tab_DIST_1(x,y))))
print("Coupure (x,y) : %d"%(coupure(x,y)))
print("----------------------")

x ="AGTACGCA"
y ="TATGC"

dist = Tab_DIST_1(x,y)
print("Distance d'édition")
for i in dist:
    print("" + str(i))

print("Mot x :%s"%(x))
print("Mot y :%s"%(y))
print("Un alignement de (x,y): ( %s , %s )"%(SOL_1(x,y,Tab_DIST_1(x,y))))
print("Coupure (x,y) : %d"%(coupure(x,y)))
print("----------------------")