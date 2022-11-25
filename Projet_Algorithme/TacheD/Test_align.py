from align import align_lettre_mot

##Test

x = "A"
y = "ATGC"
print("Mot x :%s"%(x))
print("Mot y :%s"%(y))
print("Un alignement de (x,y): \n( %s )"%(align_lettre_mot(x,y)))
print("----------------------")

x = "A"
y = "TTGCCT"
print("Mot x :%s"%(x))
print("Mot y :%s"%(y))
print("Un alignement de (x,y): \n( %s )"%(align_lettre_mot(x,y)))
print("----------------------")

x = "C"
y = "ATTA"
print("Mot x :%s"%(x))
print("Mot y :%s"%(y))
print("Un alignement de (x,y): \n( %s )"%(align_lettre_mot(x,y)))
print("----------------------")
