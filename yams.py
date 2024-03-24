import random
import os
from tkinter import Tk, Button, Label


class Dé: #classe pour les dés

     def __init__(self):
        os.system('cls')
        self.dmax = 6 #valeur maximum
        self.dmin = 1 # valeur minimum
        self.valeur = [0,0,0,0,0] #valeur du dé
        self.dnbr = 5 #nombre de dé
        self.dnbrrl = 3 #nombre de relance possible
        self.total = 0 #score total
        self.dnum = 1 # numéro du dé
        self.egal = 0 # nbr dé égaux
        self.suite = 0 # nbr de dé au chiffres qui se suivent pour définir petite ou grande suite
        self.restecombi = ["1", "2", "3", "4", "5", "6", "brelan",
                            "carré","full", "petite suite", 
                            "grande suite", "yams", "chance"] # liste des combinaisons restante

     def tirage(self): #random la valeur de chaque dé
          for i in range(self.dnbr):
               self.valeur[i] = random.randint(self.dmin, self.dmax)
          self._classer()

          return str(self.valeur) + "\n" + "combinaison possible :"+str(self.combinaison())
     

     def relance(self): # permet de relancer un ou plusieurs dé
          while self.dnbrrl >=1:
               self.dnbrrl -= 1
               print("nombre de relance possible : " + str(self.dnbrrl))
               for i in range(self.dnbr):
                    self.dnum = i
                    a = input("relancer le dé n°"+ str(i+1) + "? (oui(a)/non(entrer)) ")
                    if a == "a":
                         self.valeur[i] = random.randint(self.dmin, self.dmax)
                    else:
                         pass
               self._classer()
               
               return str(self.valeur) + "\n" + str(self.combinaison())
          
          
     def _classer(self): #classe les valeurs dans l'ordre croissant
          self.valeur.sort()

          return self.valeur
     
     def score(self): #gestion du score tour / total
          try:
               self.point = int(input("Points :"))
               self.total += self.point
          except ValueError:
               print("rentrer une valeur exacte")
               t.score()

          return "points du tour : " + str(self.point) + "// TOTAL : " + str(self.total)

     def combinaison(self): # analyse les dé et recherche des combinaisons
          self.egal = 0
          self.suite = 0

          for i in range(self.dnbr):
             for j in range(self.dnbr):
                   if self.valeur[i] == self.valeur[j] and i!=j:
                         self.egal += 1
                    
          for i in range(0,4):
               if self.valeur[i] == (self.valeur[i+1] - 1):
                    self.suite +=1
                    

          match self.egal: # nbr valeur égal * nbr valeur égal - 1
              case 6:
                    return "brelan"
                   
              case 12:
                    return "carré"
                   
              case 8:
                    return "full -> 25 pts"
                   
              case 20:
                    return "! Yams !"
                   
          match self.suite:
               case 3:
                    return "petite suite -> 30 pts"
                    
               case 4:
                    return "grande suite -> 40 pts"
                    
     
     def liste(self): #permet de voir ce qu'il reste a réaliser comme combinaison
          if len(self.restecombi) > 0:
               try:
                    print(self.restecombi)
                    x = str(input("nom de la combinaison à retirer : "))
                    self.restecombi.remove(x)

               except ValueError:
                    print("cette combinaison n'existe pas ou a été déjà réalisé")
                    t.liste()
          else:
               print("fin de jeu ! Points : " + self.total)

          return self.restecombi
     

class Interface(Tk): #classe pour l'interface graphique
     def __init__(self):
          super().__init__()
          label = Label(self,text="Jeu de Yams")
          label.pack()
          self.title("Yams !")
          self.geometry("500x100")
     
     def home(self):
          button = Button(self, text="Jouer!",command = start)
          button.pack()
     
     def Itirage(self):
          self.Iclear()
          self.valeur = Label(self,text = t.valeur)
          self.valeur.pack()

     def Irelance(self):
          self.titre = Label(self,text = "relancer le dé n°" + str(t.dnum))
          self.oui = Button(self, text="oui")
          self.non = Button(self, text="non")
          self.oui.pack()
          self.non.pack()
          self.titre.pack()

     def Iclear(self):
          for widget in self.winfo_children():
               widget.destroy()


def start(): #fonction pour lancer et faire tourner le programme -> appel la classe Dé
     while len(t.restecombi) > 0:

          s = input("lancer le tirage des dés (a) // quitter(z) // liste combinaison restante(e): ")
          
          if s == "a":
               os.system('cls')
               print(t.tirage())
               while t.dnbrrl >=1:
                    print(t.relance())
               t.dnbrrl = 3
               print(t.score())
               t.liste()

          elif s == "z": #Exit
               break
          
          elif s == "e": #liste combinaison
               print(t.restecombi)
     print("\n Fin du jeu ! Tu as " + str(t.total) + " points !")




t = Dé()
print("Pour jouer, appuyer sur les touches inscrites entre parenthèse : action(touche)")
start()


