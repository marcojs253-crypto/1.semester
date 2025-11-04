import random
import pygame
import math
from collections import Counter  # NY: Til majoritet i kNN

class data_point:
    def __init__(self, x_værdie, y_værdie, class_label, color):
        self.x_værdie = x_værdie
        self.y_værdie = y_værdie
        self.class_label = class_label
        self.color = color
    
    def metod_draw(self, screen):  # Tilføj 'screen' parameter
        pygame.draw.circle(screen, self.color, (int(self.x_værdie), int(self.y_værdie)), 10)

# NY: kNN-klasse (opgave 6)
class knn_klassifikator:
    def __init__(self, k=3):
        self.k = k
    
    def afstand(self, punkt1, punkt2):
        dx = punkt1.x_værdie - punkt2.x_værdie
        dy = punkt1.y_værdie - punkt2.y_værdie
        return math.sqrt(dx**2 + dy**2)
    
    def klassificer(self, nyt_punkt, alle_punkter):
        afstande = []
        for punkt in alle_punkter:
            dist = self.afstand(nyt_punkt, punkt)
            afstande.append((punkt, dist))
        afstande.sort(key=lambda par: par[1])
        nærmeste_labels = [par[0].class_label for par in afstande[:self.k]]
        majoritet = Counter(nærmeste_labels).most_common(1)[0][0]
        return majoritet

# Opgave 1-2 & 5: Salmon (10 stk)
liste_med_punkter = []
for laks in range(10):
    x = random.gauss(200, 20)
    y = random.gauss(200, 20)
    liste_med_punkter.append(data_point(x, y, "salmon", (255, 10, 10)))

# Opgave 5: Sea bass (10 stk, tilføj til samme liste)
for sea_bass in range(10):
    x = random.gauss(400, 20)
    y = random.gauss(200, 20)
    liste_med_punkter.append(data_point(x, y, "sea bass", (100, 10, 10)))

# Opgave 7: Et nyt enkelt punkt (ikke tilføj til liste, label None)
nyt_punkt = data_point(240, 150, None, (0, 255, 10))

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

main()
