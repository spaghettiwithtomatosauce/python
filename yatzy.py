# Erik, Johannes och Gustav Yatzy T23

# IMPORTERADE LIBRARIES
import random

# GlOBALA LISTOR
tärningar = []

# VARIABLER

# DICTIONARIES 
dict_spelare_poäng = {}

# FUNKTIONER

# Tärningslag
def tärning():
    #Ta ett nummer 1-6
    tärningslag = random.randint(1,6)
    print(f"{tärningslag}")
    #Lägg nummret som slagits i globala listan tärningar
    tärningar.append(tärningslag)
    

# Femmor
def femmor():
    if 5 in tärningar:
        längd = len(tärningar)
        tärningar.remove(5)
        resultat = längd - len(tärningar)

def stege():
    if range(1, 6) or range(2, 7) in tärningar:
        
# Kallas på när man vill välja hur många spelare, och sparar mängden i ett dictionary
def antal_spelare():
    while True:
        antal_spelare = int(input("Hur många ska spela Yatzy?\nTryck 2 för 2 spelare, 3 för 3 och 4 för 4: "))
        if antal_spelare == 2:
            # Lägger in spelarna i ett dictionary, värdet är noll för båda då det är spelarnas startpoäng
            dict_spelare_poäng.update({f"spelare1": 0, "spelare2": 0,})
            print(f"Två spelare har valt.")
            break
        elif antal_spelare == 3:
            dict_spelare_poäng.update({f"spelare1": 0, "spelare2": 0,"spelare3": 0,})
            print(f"Tre spelare har valts.")
            break
        elif antal_spelare == 4:
            dict_spelare_poäng.update({f"spelare1": 0, "spelare2": 0,"spelare3": 0, "spelare4": 0,})
            break
        else:
            print("Ogiltigt värde")
            
def starta_spel():
    antal_spelare()


    
# SPELETS GÅNG
# Startskärm. Tryck för att starta (spelar ingen roll vad användaren trycker)
start = input("Välkommen till Yatzy!\nTryck 'Enter' för att börja spela: ")
starta_spel()
