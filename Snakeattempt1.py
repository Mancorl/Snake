import pygame # importerer pygame modulen, som lar oss bruke veldig mange nyttige moduler, herunder vinduet selve spillet skjer i
import time # Importerer tidsmodulen som lar oss programmere IHHT tid
import random #Importerer random modulen, som lar oss definere tilfeldige verdier
pygame.init()#initialiserer pygame som lar oss bruke alle modulene i pygame. Trenger dette for å tegne slangen og maten 
gameon=True #setter while variabel slik at vi kan avbryte while løkken spillet foregår i senere
(width,height) = (1280,720)#Definerer bredde og høyde til vinduet spellet foregår i som en tuppel da pygame krever tuppel
background_color = (0,0,0) #Definerer bakgrunnsfargen til spillet som helt svart
screen = pygame.display.set_mode((width, height))# Definerer vinduet spillet skjer i, initierer med tuppelen definert over
pygame.display.set_caption("Snake")#Setter navnet til vinduet spillet skjer i som snake
FPS = 60#Definerer en variabel som lar oss bestemme hvor ofte spillvinduet oppdaterer. Startverdi vil være 60 ganger i sekundet
x = 640 #Definerer startposisjonen til slangen som midt på x-aksen
y = 360 #Definerer startposisjonen til slangen langs y-aksen sammen med x-aksen starter slangen midt på skjermen
snekmove = 4 #bevegelsesfaktor for slangen. nyttig for å definere hastigheten slangen beveger seg i og hvor maten kan være
direction = "down"#definerer retning og gir en default verdi, slik at slangen beveger seg til å begynne med
Snake_food_eaten = 0#Definerer en variabel som lar oss holde styr på hvor mye slangen vår har spist
ont = pygame.font.SysFont(None, 26)#Setter fonten som brukes i dette programmet til å være standardfonten til maskinen det kjører på og i en passende størrelse
Snakehead = ont.render('Q', True, (255,255,255))#Setter grafikken for slangens hode til bokstaven Q (streken gjennom q ser ut som en tunge)
clock = pygame.time.Clock() #initialiserer en klokkefunskjon som lar oss sette en FPS cap, slik at vi ikke stresser systemet så mye
Snekfood = False#denne variabelen sier at det ikke eksisterer slangemat på skjermen
food = ont.render('F',True,(255,255,255))#Setter grafikken for slangens mat itil å være standardfonten til maskinen og i en passende størrelse og hvitt i kontrast til bakgrunnen
(xsw,ysh) = Snakehead.get_size()#finner størelsen på slangehodet. lar meg også endre størrelsen uten konsekvenser for spillet
(afw,yfh) = food.get_size()#Samme som over bare for slangens mat
Snekbody = ont.render('o', True, (255,255,255))

while gameon:#Starter while løkken spillet skjer i

    #toppen her gir noen viktige definisjoner og avklarer alt før vi faktisk spiller for hver iterasjon av while løkken
    clock.tick(FPS)/1000#Setter frekvensen mellom hver gang spillvinduet oppdaterer til 1/60 av ett sekund (60 ganger over 1000 millisekund)
    screen.fill(background_color)#Fyller skjermen med bakgrunnsfargen som ble definert over
    (w,h) = screen.get_size() #definerer variabler w og h som gir oss bredde og høyde av vinduet
    ### Starten av det faktiske spillet

    ### Under definerer vi retningen slangen skal bevege seg i
    move = pygame.key.get_pressed() # gir oss en liste over taster som blir trykket
    if move[pygame.K_w]:#Dersom w trykkes blir retningen satt som opp
        direction = "up"
    elif move[pygame.K_UP]:#Dersom piltast opp trykkes blir retningen satt som opp
        direction = "up"
    if move[pygame.K_s]:#Dersom s trykkes blir retningen satt som ned
        direction = "down"
    elif move[pygame.K_DOWN]:#Dersom piltast ned trykkes blir retningen satt som ned
        direction = "down"
    if move[pygame.K_a]:#Dersom a trykkes blir retningen satt som venstre
        direction = "left"
    elif move[pygame.K_LEFT]:#Dersom piltast venstre trykkes blir retningen satt som venstre
        direction = "left"
    if move[pygame.K_d]:#Dersom d trykkes blir retningen satt som høyre
        direction = "right"
    elif move[pygame.K_RIGHT]:#Dersom piltast høyre trykkes blir retningen satt som høyre
        direction = "right"

    ### Under utføres utretningen som ble definert over, det er viktig å huske at posisjonen (0,0) er øverst til venstre i vinduet
    ### Dette fører til at når y blir lavere vil slangen bevege seg nedover og når x blir høyere beveger slangen seg mot høyre.
    ### slik at lavere y noe uintuitivt er høyere på skjermen

    if direction == "up":#Utfører retningen definert i if else setningene over her setter den retningen opp, for å gjøre dette subtraheres y verdien
        y = y - snekmove
        
        Snakehead = pygame.transform.rotate(ont.render('Q', True, (255,255,255)), 180)#Roterer slangehodet 180 grader når slangen beveger seg oppover
        if y < 0:#Dersom y blir så lav at Q(slangehodet) går ut av skjermen setter vi posisjonen til Q til bunnen av vinduet
            y = h + y
    elif direction == "down":#Utfører retningen definert i if else setningene over her setter den retningen ned, for å gjøre dette adderes y verdien
        y = y + snekmove
        
        Snakehead = ont.render('Q', True, (255,255,255))#Passer på at slangehodet ikke er rotert når det beveger seg nedover
        if y > h:#Dersom y blir så høy at Q(slangehodet) går ut av skjermen setter vi posisjonen til Q til toppen av vinduet
            y = h - y
    elif direction == "left":#Utfører retningen definert i if else setningene over her setter vi retningen som venstre, for å gjøre dette subtraheres x verdien
        x = x - snekmove
        Snakehead = pygame.transform.rotate(ont.render('Q', True, (255,255,255)), 270)#Roterer slangehodet 270 grader når slangen beveger seg oppover
        if x < 0:#Dersom x blir så lav at Q(slangehodet) går ut av skjermen setter vi posisjonen til Q til høyresiden av vinduet
            x = w + x
    elif direction == "right":#Utfører retningen definert i if else setningene over her setter den retningen høyre, for å gjøre dette adderes x verdien
        x = x + snekmove
        Snakehead = pygame.transform.rotate(ont.render('Q', True, (255,255,255)), 90)#Roterer slangehodet 90 grader når slangen beveger seg oppover
        if x > w:#Dersom x blir så høy at Q(slangehodet) går ut av skjermen setter vi posisjonen til Q til venstresiden av vinduet
            x = w - x
    if Snekfood == False:
        b = random.randint(0,h +( 5* snekmove))#definerer tilfeldige høydekoordinater for maten til slangen. ettersom slangen endrer posisjon, med litt margin slik at maten ikke gjemmer seg i kantene
        a = random.randint(0,w - snekmove)
        print(a,b,Snake_food_eaten)#For debugging
        Snekfood = True#Slangematen eksisterer nå
        
    ###Kollisjon mellom slangens hode og mat
    if Snekfood == True:#Dersom slangematen eksisterer skal vi sjekke for kollisjon med slangens hode. Slangemat skal alltid eksistere her, da if statement over garanterer at det er sant.
        if x >= a -1:#Dersom slangens lengst venstreliggende punkt ligger til høyre(eller på) for matens lengst venstreliggende punkt + litt margin
            if x <= a + afw + 1:#Dersom slangens lengst venstreliggende punkt ligger til venstre (eller på) for matens lengst høyreliggende punkt + litt margin
                if y >= b - yfh:#Dersom slangens høyeste punkt ligger over eller på matens lavest liggende punkt
                    if y <= b:#Dersom slangen høyest liggende punkt ligger lavere enn eller på matens laveste punkt 
                        Snekfood = False#Skal slangematen ikke eksistere lenger slik at den får nye koordinater
                        Snake_food_eaten = Snake_food_eaten + 1 #Skal også slangen få spise litt mat
                if y - ysh >= b - yfh:#Dersom slangens nederste punkt derimot ligger over matens nederste punkt 
                    if y - ysh <= b:# og slangens nederste punkt ligger under matens nederste punkt
                        Snekfood = False#skal maten fortsatt slettes og
                        Snake_food_eaten = Snake_food_eaten + 1#Fortsatt slangen spise maten sin                   
        if x + xsw >= a -1:#Dersom slangens lengst høyreliggende punkt ligger til høyre for matens lengst venstreliggende punkt + litt margin
            if x + xsw <= a + afw + 1:#Og slangens lengst høyreliggende punkt ligger til venstre for matens lengst høyreliggende punkt + litt margin
                if y >= b - yfh:#og slangens øverste punkt ligger over matens nederste punkt
                    if y <= b:#og slangens øverste punkt ligger under matens øverste punkt
                        Snekfood = False#skal maten slettes
                        Snake_food_eaten = Snake_food_eaten + 1#og slangen spise
                if y - ysh >= b - yfh:#dersom slangens nederste punkt ligger over matens nederste punkt
                    if y - ysh <= b:#og slangens nederste punkt ligger under matens øverste punkt
                        Snekfood = False#Skal maten fortsatt slettes
                        Snake_food_eaten = Snake_food_eaten + 1# og slangen fortsatt spise

                
    screen.blit(food,(a,b))#tegner Slangematen på de oppgitte koordinatene
    screen.blit(Snakehead,(x,y))# tegner slangehodet på de oppgitte kooridnatene
    pygame.display.flip()#Oppdaterer spillvinduet slik at alle tegneinstruksjonene jeg har gitt så langt vises

    #Sjekker om spilleren har lyst til å avslutte
    for event in pygame.event.get():#Starter en løkke som søker gjennom events i pygame modulen
        if event.type == pygame.QUIT:#Dersom eventen er pygame.quit dvs dersom vi trykker på x i hjørnet er denne sann
            gameon = False#Dersom eventen over er sann setter vi variabelen vår slik at while løkken brytes
        
#class snake():

    #fda
