import matplotlib.pyplot as plt
import math
from prettytable import PrettyTable


class Zufallsgröße():

    def __init__(self, Name, WerteZG, WSKWerteZG):
        self.Name = Name
        self.xi = WerteZG
        self.Pxi = WSKWerteZG


    def WerteZufallsgröße(self):
        return(self.xi)


    def Wahrscheinlichkeitsfunktion(self):
        return(self.Pxi)


    def Stabdiagramm(self):
        plt.figure()
        plt.bar(self.xi, self.Pxi, width= 0.1)
        plt.get_current_fig_manager().set_window_title("Stabdiagramm W("+self.Name+")")
        plt.title("Stabdiagramm W("+self.Name+")")
        plt.xlabel("xi")
        plt.ylabel("P("+ self.Name+"= xi)")
        plt.show(block = False)


    def Histogramm(self, Rechteckbreite):
        heights = []
        for element in self.Pxi:
            height = element / Rechteckbreite
            heights.append(height)

        plt.figure()
        plt.bar(self.xi, heights, width= Rechteckbreite)
        plt.get_current_fig_manager().set_window_title("Histogramm W("+self.Name+")")
        plt.title("Histogramm W("+self.Name+")")
        plt.xlabel("xi")
        plt.ylabel("P("+ self.Name+"= xi)")
        plt.show(block = False)


    def kumlativeVerteilungsfunktion(self):
        VerteilungsfunktionWerte = []
        VerteilungsfunktionWerte.append(self.Pxi[0])

        i = 1
        while i < len(self.Pxi):
                Wert = self.Pxi[i] + VerteilungsfunktionWerte[i-1]
                VerteilungsfunktionWerte.append(Wert)
                i = i+1

        return VerteilungsfunktionWerte

        
    def Treppenfunktion(self):
        x = self.xi
        F = self.kumlativeVerteilungsfunktion()

        plt.step(x,F, where= "post", color= "blue")  
        plt.scatter(x,F, color ="blue", s= 100)
        plt.get_current_fig_manager().set_window_title("Treppenfunktion T("+self.Name+")")
        plt.title("Treppenfunktion T("+self.Name+")")
        plt.xlabel("xi")
        plt.ylabel("T("+ self.Name+")")
        plt.show(block= False)


    def Erwartungswert(self):
        E = 0
        i = 0
        while i <  len(self.xi):
            E = E + self.xi[i] * self.Pxi[i]
            i = i+1
        
        return E


    def Varianz(self):
        E = self.Erwartungswert()
        i = 0
        V = 0
        while i < len(self.xi):
            V = V + (self.xi[i] - E)**2 * self.Pxi[i]
            i = i +1

        return V


    def Standardabweichung(self):
        return math.sqrt(self.Varianz())
        

    def Tabelle(self):
        table = PrettyTable()

        table.field_names = ["Was","Werte"]
        table.add_row(["xi", self.xi])
        table.add_row(["P("+self.Name+"= xi)", self.Pxi])
        table.add_row(["P("+ self.Name+" <= xi)", self.kumlativeVerteilungsfunktion()])
        table.add_row(["E("+self.Name +")", self.Erwartungswert()])
        table.add_row(["Var("+ self.Name +")", self.Varianz()])
        table.add_row(["{sigma}", self.Standardabweichung()])

        print("Tabelle für die Zufallsgröße "+ self.Name)
        print(table)