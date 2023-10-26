
# funktion för antal spelare
def antal_spelare(): 
    # Definerar en dictionary
    databas = {}
    # definerar två grundläggande variabler
    spelarnummer = 1
    spelarpoäng = 0
    # en loop som körs så länge inputen inte är den önskade. I detta fall frågar programmet hur många spelare som finns.
    while True:
        
        try: 
            # input för hur många seplare vi är
            antal = int(input("Hur många spelare är ni? Ni får bara vara 2-4 spelare: "))
            # om antal är mellan 2 och 5 så avslutas loopen och programmet kan gå vidare.
            if antal in range(2, 5):
                break
            # om antalet man skriver in är mindre än 2 körs loopen igen
            elif antal < 2:
                print("Ni måste vara minst 2")
                pass
            # om antalet man skriver in är större än 4 körs loopen igen
            elif antal > 4:
                print("Ni får inte vara fler än 4")
                pass
        # programmet testar om det är en string istället för en integer, då körs loopen igen
        except ValueError:
            print("Skriv en integer, inte string!")
            pass
    # loop som körs från 1 till hur många spelare det finns plus ett
    for i in range(1, antal + 1):
        # updattera dictionaryt databas och där den ska fråga om vårat namn, och sedan lägger till våran poäng som value
        databas.update({input(f"Vad heter spelare {spelarnummer}?"): spelarpoäng})
        # man ändrar spelarnumret till ett högre för att den inte ska köra i oändlighet
        spelarnummer = spelarnummer + 1
    # inte nödvändingt, men utskriften visar att den har sparat våra namn med en poäng i databas
    print(databas)
    # returnar databas dictionaryt
    return databas
# kalla på funkitonen databas för att proggrammet ska köras
antal_spelare()
