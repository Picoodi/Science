import matplotlib.pyplot as plt
from ClassZufallsgröße import Zufallsgröße


######Hier der Code zwischen den #
# Zufallsgröße mit Name = Zufallsgröße("Name", [Werte], [WSK])
#Bsp 
# X = Zufallsgröße("X", [-1,0,3,5], [1/4, 1/6, 5/6, 1/4])

#Man kann nun verschiedene funktionen callen:
# Name.Wertezufallsgröße()                      
# Name.Wahrscheinlichkeitsfunktion()
# Name.Stabdiagramm()
# Name.Histogramm(Rechteckbreite)
# Name.kumulativeVerteilungsfunktion()
# Name.Treppenfunktion()
# Name.Erwartungswert()
# Name.Varianz()
# Name.Standardabweichung()
# Name.Tabelle()    -> gibt alles im Überblick zurück

###############################################################

C = Zufallsgröße("Chem" ,[-10, 350], [36/37, 1/37])
H = Zufallsgröße("Hanna", [-10, 10], [19/37, 18/37])
print(C.Tabelle(), H.Tabelle())
H.Histogramm(1)


#############################################################

#Code ist notwenig damit matplolib diagramme bleiben solang ach das programm läuft
while plt.get_fignums():
    plt.pause(0)