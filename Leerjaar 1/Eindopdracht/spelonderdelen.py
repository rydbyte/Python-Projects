import random as random #de random module voor de kaarten shuffle

class cards: #object kaarten met alle kaarten erin
    
    #object kaarten met properties naam en value
    class harten_aas:
        name = "\u2764\uFE0F"+"  aas"#\u voor de emojis
        value = 10

    class harten_heer:
        name = "\u2764\uFE0F"+"  heer"
        value = 10

    class harten_dame:
        name = "\u2764\uFE0F"+"  dame"
        value = 10

    class harten_boer:
        name = "\u2764\uFE0F"+"  boer"
        value = 10
        
    class harten_10:
        name = "\u2764\uFE0F"+"  10"
        value = 10
        
    class harten_9:
        name = "\u2764\uFE0F"+"  9"
        value = 9
        
    class harten_8:
        name = "\u2764\uFE0F"+"  8"
        value = 8
        
    class harten_7:
        name = "\u2764\uFE0F"+"  7"
        value = 7
        
    class harten_6:
        name = "\u2764\uFE0F"+"  6"
        value = 6

    class harten_5:
        name = "\u2764\uFE0F"+"  5"
        value = 5
        
    class harten_4:
        name = "\u2764\uFE0F"+"  4"
        value = 4
        
    class harten_3:
        name = "\u2764\uFE0F"+"  3"
        value = 3

    class harten_2:
        name = "\u2764\uFE0F"+"  2"
        value = 2
        

    class ruiten_aas:
        name = "\u2666\uFE0F"+"  aas"
        value = 10

    class ruiten_heer:
        name = "\u2666\uFE0F"+"  heer"
        value = 10

    class ruiten_dame:
        name = "\u2666\uFE0F"+"  dame"
        value = 10

    class ruiten_boer:
        name = "\u2666\uFE0F"+"  boer"
        value = 10
        
    class ruiten_10:
        name = "\u2666\uFE0F"+"  10"
        value = 10
        
    class ruiten_9:
        name = "\u2666\uFE0F"+"  9"
        value = 9
        
    class ruiten_8:
        name = "\u2666\uFE0F"+"  8"
        value = 8
        
    class ruiten_7:
        name = "\u2666\uFE0F"+"  7"
        value = 7
        
    class ruiten_6:
        name = "\u2666\uFE0F"+"  6"
        value = 6

    class ruiten_5:
        name = "\u2666\uFE0F"+"  5"
        value = 5
        
    class ruiten_4:
        name = "\u2666\uFE0F"+"  4"
        value = 4
        
    class ruiten_3:
        name = "\u2666\uFE0F"+"  3"
        value = 3

    class ruiten_2:
        name = "\u2666\uFE0F"+"  2"
        value = 2


    class klaver_aas:
        name = "\u2663\uFE0F"+"  aas"
        value = 10

    class klaver_heer:
        name = "\u2663\uFE0F"+"  heer"
        value = 10

    class klaver_dame:
        name = "\u2663\uFE0F"+"  dame"
        value = 10

    class klaver_boer:
        name = "\u2663\uFE0F"+"  boer"
        value = 10
        
    class klaver_10:
        name = "\u2663\uFE0F"+"  10"
        value = 10
        
    class klaver_9:
        name = "\u2663\uFE0F"+"  9"
        value = 9
        
    class klaver_8:
        name = "\u2663\uFE0F"+"  8"
        value = 8
        
    class klaver_7:
        name = "\u2663\uFE0F"+"  7"
        value = 7
        
    class klaver_6:
        name = "\u2663\uFE0F"+"  6"
        value = 6

    class klaver_5:
        name = "\u2663\uFE0F"+"  5"
        value = 5
        
    class klaver_4:
        name = "\u2663\uFE0F"+"  4"
        value = 4
        
    class klaver_3:
        name = "\u2663\uFE0F"+"  3"
        value = 3

    class klaver_2:
        name = "\u2663\uFE0F"+"  2"
        value = 2
        
    
    class schoppen_aas:
        name = "\u2663\uFE0F"+"  aas"
        value = 10

    class schoppen_heer:
        name = "\u2663\uFE0F"+"  heer"
        value = 10

    class schoppen_dame:
        name = "\u2663\uFE0F"+"  dame"
        value = 10

    class schoppen_boer:
        name = "\u2663\uFE0F"+"  boer"
        value = 10
        
    class schoppen_10:
        name = "\u2663\uFE0F"+"  10"
        value = 10
        
    class schoppen_9:
        name = "\u2663\uFE0F"+"  9"
        value = 9
        
    class schoppen_8:
        name = "\u2663\uFE0F"+"  8"
        value = 8
        
    class schoppen_7:
        name = "\u2663\uFE0F"+"  7"
        value = 7
        
    class schoppen_6:
        name = "\u2663\uFE0F"+"  6"
        value = 6

    class schoppen_5:
        name = "\u2663\uFE0F"+"  5"
        value = 5
        
    class schoppen_4:
        name = "\u2663\uFE0F"+"  4"
        value = 4
        
    class schoppen_3:
        name = "\u2663\uFE0F"+"  3"
        value = 3

    class schoppen_2:
        name = "\u2663\uFE0F"+"  2"
        value = 2
        
deck = [#stopt alle objecten in de deck list

    cards.harten_aas,
    cards.harten_heer,
    cards.harten_dame,
    cards.harten_boer,
    cards.harten_10,
    cards.harten_9,
    cards.harten_8,
    cards.harten_7,
    cards.harten_6,
    cards.harten_5,
    cards.harten_4,
    cards.harten_3,
    cards.harten_2,

    cards.ruiten_aas,
    cards.ruiten_heer,
    cards.ruiten_dame,
    cards.ruiten_boer,
    cards.ruiten_10,
    cards.ruiten_9,
    cards.ruiten_8,
    cards.ruiten_7,
    cards.ruiten_6,
    cards.ruiten_5,
    cards.ruiten_4,
    cards.ruiten_3,
    cards.ruiten_2,

    cards.klaver_aas,
    cards.klaver_heer,
    cards.klaver_dame,
    cards.klaver_boer,
    cards.klaver_10,
    cards.klaver_9,
    cards.klaver_8,
    cards.klaver_7,
    cards.klaver_6,
    cards.klaver_5,
    cards.klaver_4,
    cards.klaver_3,
    cards.klaver_2,

    cards.schoppen_aas,
    cards.schoppen_heer,
    cards.schoppen_dame,
    cards.schoppen_boer,
    cards.schoppen_10,
    cards.schoppen_9,
    cards.schoppen_8,
    cards.schoppen_7,
    cards.schoppen_6,
    cards.schoppen_5,
    cards.schoppen_4,
    cards.schoppen_3,
    cards.schoppen_2,
    ]


class dealer: #object voor de dealer
   dealers_hand = []#list waaar alle dealers kaarten in gaan
   
   def check():#functie voor het checken 
        
        totaal_dealer = dealer.dealers_hand[0].value+dealer.dealers_hand[1].value#totaale dealer is van de dealer hand list eerste + tweede waaarbij het van het object de proprty value pakt
        
        if totaal_dealer > 21:# als de totaale value meer is dan 21 dan wint de speler
            print("jij wint")
            exit()

        return totaal_dealer# geeft het tottaal terug


class player:#object speler
    players_hand = []#spelers hand list
    heeft_aas = False#boolean voor het checken van een aas

    def check():# functie voor het checken
        player_amount_cards = len(player.players_hand)# totalle hoeveelheid kaarten
        totaal_player = 0# begint met een totaale value van 0
        
        for amount in range(player_amount_cards):# for loop die die werkt op hoeveel kaarten een speler heeft geen idee hoe het werkt als de begin van een list [0] is maar het werkt dus whatever
            print(f"\n{player.players_hand[int(amount)].name}   Punten: {player.players_hand[int(amount)].value}")#print op volgore van [0] got hoeveel kaarten ee speler heeft daarvan de naam en de punten die de kaart geeft
            totaal_player = totaal_player+player.players_hand[amount].value# de totaal hoeveelheid punten opgetelt
            if player.players_hand[amount].name == "\u2764\uFE0F"+"  aas" or player.players_hand[amount].name == "\u2666\uFE0F"+"  aas" or player.players_hand[amount].name == "\u2663\uFE0F"+"  aas" or player.players_hand[amount].name == "\u2663\uFE0F"+"  aas":#als een speler een van de volgonde 4 asen heeft word gecehceck door door de hand list van de speler te gaan en de objecens hun naam property te checken 
                player.heeft_aas = True#verandert de bool variable naar waar
            
        print(f"Jouw totale punten:\n{totaal_player}\n\n")# print de totalle hoeveelheid met format linebreak 
        print(f"Dealers totale punten:\n{dealer.dealers_hand[0].value + dealer.dealers_hand[1].value}\n")#print de dealers totale hoeveeilheid punten  door naar de dealers hand list te gaan en dan de eerrste en tweede op te tellen van objecten.value
        if totaal_player > 21 and not player.heeft_aas:# als het totall van de speler over 21 punten gaat en hij geen is heeft de bool value false is 
            print("Game over")# game over
            exit()
        elif totaal_player > 21 and player.heeft_aas:# anders als heeft over 21 gaat en de bool variable wel true is
            verander = input("Je gaat over de 21 punten maar hebt een aas wil je je aas als 1 punt laten tellen? \n1.Ja\n2.Nee\n")#vraagt de speler of ze de asen van 10 punten naar  willen veranderen
            if verander == "1":#als de speler 1(ja) zegt 
                player.heeft_aas = False#voor zekerheid de aas value op false zetten
                totaal_player = 0# zet het totale terug naar 0 omdat het opnieuw berekent moet worden
                for amount in range(player_amount_cards):#ik had dit gewoon een functie moeten maken inplaats van kopieren.....
                    if player.players_hand[amount].name == "\u2764\uFE0F"+"  aas" or player.players_hand[amount].name == "\u2666\uFE0F"+"  aas" or player.players_hand[amount].name == "\u2663\uFE0F"+"  aas" or player.players_hand[amount].name == "\u2663\uFE0F"+"  aas":#checkt voor de aas door door de hand list te loopen
                        player.players_hand[amount].value = 1#zet de aas value naar 1

                    print(f"\n{player.players_hand[int(amount)].name}   Punten: {player.players_hand[int(amount)].value}")#print voor alle kaarten opnieuw naam en punten
                    
                    totaal_player = totaal_player+player.players_hand[amount].value#berekent het totale opnieuw maar nu met aas 1 punt
                
                print(f"Jouw totale punten:\n{totaal_player}\n\n")# print het totaale met het totaal variable
                if totaal_player > 21:#als het totaal nog steeds over 21 gaat
                        print(f"Dealers totale punten:\n{dealer.dealers_hand[0].value + dealer.dealers_hand[1].value}\n")#print de dealers totale punten
                        print("Game over")
                        exit()
                elif totaal_player < 21:#als het niet meer over 21 gaat
                        totaal__dealer = dealer.check()#checkt de dealer en geeft de totaale punten van de dealers hand list terug
                        print(f"Dealers totale punten:\n{totaal__dealer}\n")#print de dealers kaarten punten
                        if totaal_player > totaal__dealer:# als het totaal van de speler hoger is dan dat van de dealer dan gewonnen
                            print("Gewonnen!")
                            exit()
            else:#als een speler niet de aas naar 1 wilt veranderen
                print("Game over")
                exit()

        return totaal_player#geeft de totaale hoeveelheid punten terug
       

class deck_:#object waar alle functies voor het deck inzitten

    def shuffle():#functie voor de shuffle
       random.shuffle(deck)#van de random module pak de shuffle functie

    def hit(target):#voor kaarten geven
         given_card = deck.pop(0)#popt haalt kaart uit deck en returend de value pakt de eerste van het deck
         if target == "dealer":#als de meeggeven info de string dealer is dan geef kaart aan dealer
            dealer.dealers_hand.append(given_card)
         else:# als de meegegeven info geen "dealer" is
            player.players_hand.append(given_card)#stopt in de players hand list de given_card dat de returned value is van het deck
            player.check()#checkt de speler functie

    def start():#functie voor waneer het spel begint
        deck_.shuffle()#shuffled
        deck_.hit("dealer")#hit de dealer
        print(f"\nDe dealer pakt een kaart\n{dealer.dealers_hand[0].name}   Punten: {dealer.dealers_hand[0].value}")# print de eerste kaar van de dealers hand list naam en value
        deck_.hit("dealer")# hit de dealer opnieuw
        print(f"De dealer pakt een nog kaart\n{dealer.dealers_hand[1].name}   Punten: {dealer.dealers_hand[1].value}")#zelfde
        print(f"Dealers totale punten:\n{dealer.dealers_hand[0].value + dealer.dealers_hand[1].value}\n\n")#print de totale punten van de dealers hand list object.value
        dealer.check()#functie voor dealer checken kijken of hij over 21 gaat

    def end():# functie voor het einde
        totaal_speler = player.check()#het totaale speler variable , de functie returend de totaale waarden van de spelers hand en checkt of de speler meer punten heeft
        totaal_deler = dealer.check()#doet hetzelfde als speler functie maar van de dealers object

        if totaal_speler > totaal_deler:#als het toaal van de speler hoger is dan wint anders verliest
            print("Gewonnen!")
        else:
            print("Game over") 
            exit()




def rules():# functie voor de regels
    print(f"Welkom bij blackjack\nDe dealer pakt eerst twee kaarten en daarna mag jij pakken\nJe pakt kaarten door 1(hit) te typen, als je geen kaarten meer wilt dan type je 2(stand\nAls de dealer over 21 punten gaat dan win jij, als jij over 21 ounten gaat wint de dealer\nDe aas, heer, dame en boer zijn allemaal 10 punten en met de aas kan je bselissen tussen 10 of 1.")
