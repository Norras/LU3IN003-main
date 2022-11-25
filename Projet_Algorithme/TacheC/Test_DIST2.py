import time
import matplotlib.pyplot as plt
from DIST_2 import DIST_2
import os

# Tests

## Traitement du fichier Inst_0000010_44.adn ##
file=open("../Instances_genome/Inst_0000010_44.adn")
modx:int=int(file.readline())
mody:int=int(file.readline())
x:list[str]=file.readline().split(" ")
y:list[str]=file.readline().split(" ")
file.close()
x=x[:-1]
y=y[:-1]

print("Mot x :%s"%(x))
print("Mot y :%s"%(y))
print("Distance d'édition : %d"%(DIST_2(x,y)))
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
print("Mot x :%s"%(x))
print("Mot y :%s"%(y))
print("Distance d'édition : %d"%(DIST_2(x,y)))
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
print("Mot x :%s"%(x))
print("Mot y :%s"%(y))
print("Distance d'édition : %d"%(DIST_2(x,y)))
print("----------------------")

## Traitement du fichier Inst_0008000_98.adn ##
file=open("../Instances_genome/Inst_0008000_98.adn")
modx:int=int(file.readline())
mody:int=int(file.readline())
x:list[str]=file.readline().split(" ")
y:list[str]=file.readline().split(" ")
file.close()
x=x[:-1]
y=y[:-1]
print("Mot x :%s"%(x))
print("Mot y :%s"%(y))
print("Distance d'édition : %d"%(DIST_2(x,y)))
print("----------------------")

print("-----------------------------PERFORMANCE--------------------------------")

tab_instance = ["Inst_0000010_7.adn","Inst_0000010_8.adn","Inst_0000010_44.adn","Inst_0000012_13.adn","Inst_0000012_32.adn","Inst_0000012_56.adn","Inst_0000013_45.adn","Inst_0000013_56.adn","Inst_0000013_89.adn","Inst_0000014_7.adn","Inst_0000014_23.adn","Inst_0000014_83.adn","Inst_0000015_2.adn","Inst_0000015_4.adn","Inst_0000015_76.adn","Inst_0000020_8.adn","Inst_0000020_17.adn","Inst_0000020_32.adn","Inst_0000050_3.adn","Inst_0000050_9.adn","Inst_0000050_77.adn","Inst_0000100_3.adn","Inst_0000100_7.adn","Inst_0000100_44.adn","Inst_0000500_3.adn","Inst_0000500_8.adn","Inst_0000500_88.adn","Inst_0001000_2.adn","Inst_0001000_7.adn","Inst_0001000_23.adn","Inst_0002000_3.adn","Inst_0002000_8.adn","Inst_0002000_44.adn","Inst_0003000_1.adn","Inst_0003000_10.adn","Inst_0003000_25.adn","Inst_0003000_45.adn","Inst_0005000_4.adn","Inst_0005000_32.adn","Inst_0005000_33.adn","Inst_0008000_32.adn","Inst_0008000_54.adn","Inst_0008000_98.adn","Inst_0010000_7.adn","Inst_0010000_8.adn","Inst_0010000_50.adn","Inst_0015000_3.adn","Inst_0015000_20.adn","Inst_0015000_30.adn","Inst_0020000_5.adn","Inst_0020000_64.adn","Inst_0020000_77.adn","Inst_0050000_6.adn","Inst_0050000_63.adn","Inst_0050000_88.adn","Inst_0100000_3.adn","Inst_0100000_11.adn","Inst_0100000_76.adn"]
temps_CPU = []
len_x = []

for i in os.listdir("../Instances_genome"):
    if os.path.isfile(os.path.join("../Instances_genome", i)):
        print("Fichier : %s"%i)
        file=open("../Instances_genome/"+i)
        modx:int=int(file.readline())
        mody:int=int(file.readline())
        x:list[str]=file.readline().split(" ")
        y:list[str]=file.readline().split(" ")
        file.close()
        x=x[:-1]
        y=y[:-1]

        print("Mot x :%s"%(x))
        print("Longueur x :%d"%len(x))
        print("Mot y :%s"%(y))
        print("Longueur y :%d"%len(y))

        old_time = time.time()
        print("Distance d'edition: %d"%(DIST_2(x,y)))    
        print("Temps CPU en seconde = %d"%(time.time()-old_time))
        temps_CPU.append(time.time()-old_time)
        len_x.append(len(x))
        print("----------------------")

        if((time.time()-old_time) >= 200 ):
            print("Performance de DIST_2 en moins de 1 minutes atteint")
            break

print(len_x[0])
print(temps_CPU[0])
plt.plot(len_x,temps_CPU,'o-')
plt.xlabel("Longueur du mot x")
plt.xlim(0,20000)
plt.ylim(0,200)
plt.ylabel("Temps CPU en seconde")
plt.show()