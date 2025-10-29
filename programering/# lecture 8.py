import random
import pygame
import math
from collections import Counter
import random

screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))

class data_point:
    def __init__(self, x_værdie, y_værdie, class_label, color):
        self.x_værdie = x_værdie
        self.y_værdie = y_værdie
        self.class_label = class_label
        self.color = color
    
    def metod_draw(self):  # ÆNDRET: Tilføjet 'self' som første parameter
        pygame.draw.circle(screen, self.color, (self.x_værdie, self.y_værdie), 10)  # ÆNDRET: Bruger selvets koordinater i stedet for 'liste_med_punkter'

liste_med_punkter=[]
liste_med_single_punt=[]
for laks in range(10):
     x = random.gauss(200, 20)
     y = random.gauss(200, 20)
     liste_med_punkter.append(data_point(x,y,"salmon", (255,10,10) ))
for sea_bass in range(10):
     x = random.gauss(400, 20)
     y = random.gauss(200, 20)
     liste_med_punkter.append(data_point(x,y,"sea bass", (100,10,10) ))
for sea_bass in range(2):
     x = 240
     y = 150
     liste_med_single_punt.append(data_point(x,y,"None", (0,255,10) ))

class knn_classifier:
    def __init__(self, k=3):
        self.k = k

    def afstand( self, punkt1, punkt2):
        dx = punkt1.x_værdie - punkt2.x_værdie
        dy = punkt1.y_værdie - punkt2.y_værdie
        return math.sqrt(dx**2+dy**2)
    def klassificer(self, nyt_punkt, alle_punkter):
        afstande = []  # Liste af (punkt, afstand)
        for punkt in alle_punkter:
            dist = self.afstand(nyt_punkt, punkt)
            afstande.append((punkt, dist))
        # Sortér efter afstand (nærmeste først – sorter på andet element i parret)
        afstande.sort(key=lambda par: par[1])
        
        # Tag de k nærmeste labels (fx k=3)
        nærmeste_labels = [par[0].class_label for par in afstande[:self.k]]
        
        # Find majoritet (mest almindelige label) med Counter
        majoritet = Counter(nærmeste_labels).most_common(1)[0][0]
        return majoritet  # Returnér det mest almindelige label


# ÆNDRET: Loopet kalder nu metoden på hvert OBJEKT i listen, ikke på klassen
for punkt in liste_med_punkter:  # ÆNDRET: Bruger 'punkt' i stedet for range(len()) for klarhed
    punkt.metod_draw()  # ÆNDRET: Kalder på OBJEKTET 'punkt', ikke klassen 'data_point'
for punkt in liste_med_single_punt:  # ÆNDRET: Bruger 'punkt' i stedet for range(len()) for klarhed
    punkt.metod_draw() 
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("kNN Data Points")
    
    # NY: Opgave 6-7: Opret kNN og klassificér nyt punkt (print før loop)
    knn = knn_klassifikator(k=3)  # k=3
    forudsiget_label = knn.klassificer(nyt_punkt, liste_med_punkter)
    print(f"Det nye punkt (240, 150) klassificeres som: {forudsiget_label}")  # Fx "salmon"
    
    run_flag = True
    while run_flag is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_flag = False
        
        screen.fill((255, 255, 255))  # Ryd baggrund
        
        # Tegn alle i listen (20 prikker)
        for punkt in liste_med_punkter:
            punkt.metod_draw(screen)
        
        # Tegn nyt punkt separat
        nyt_punkt.metod_draw(screen)
        
        pygame.display.flip()
main ()





































# Exercise 9-1: Restaurant
# Make a class called Restaurant. The __init__() method for Restaurant should store
# two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information,
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance of your restaurant from your class. Print the two attributes individually,
# and then call both methods.

# Here I will write the code and corresponding comments to complete the training tasks


class Resturant:
    def __init__(self):
        self.restaurant_name= "la rosa piza"
        self.cuisine_type = "pizza"
    def describe_restaurant (self):
        print(f"navnet på restuarnten er {self.restaurant_name}, og man kan spise {self.cuisine_type}")
resturant = Resturant()
resturant.describe_restaurant ()

print(resturant.cuisine_type)




        