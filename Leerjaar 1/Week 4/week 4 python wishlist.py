
class whishlist:#whislist object
    def __init__(self, command):#functie for variables
        self.command = command

    games = {
    }#dictionary voor games
    
    def check_games(self):# functie om games te checken
            if not self.games:#als er geen games zijn
                 print("\n geen games \n")
            else:#anders als er wel games zijn
                 for amount in self.games:# print voor de hoeveelheid games
                     print(f"Name: {amount}, \n Price: {self.games[amount]}\n")#print format 

    def insert_game(self, name, price):#functie voor nieuwe game
        if name in self.games:#als de game all in the dictionary is
             print("Already in whishlist \n")
             list()
        else:#anders
            self.games[name] = price# geeft games prijs en naam
            print(f"Addded {name} to the wishlist \n Price: {price}\n")

    def total_price(self):# functie voor totale price
         cost = self.games.values()#pakt de values
         print(f"\nTotal cost: {cost} \n")

    def start(self, command):# kiest een andere functie uit met ifs
        if self.command == 1:# als 1 is ingevoerd
            self.check_games()
        if self.command == 2:# 2 ingevoerd
             game_name = input("\nGame name?: ")#naam input
             game_price = input("Game price?: ")#prijs input
             while game_price.isnumeric() == False:# als er geen nummer is ingevoerd als prijs
                  print("invalid \n")
                  game_price = input("Game price?: ")

             self.insert_game(game_name, game_price)# start de functie inser_game geeft info naam en prijs over
        if self.command == 3:# als het 3 is
             self.total_price()#berekent prijs
        if self.command == 4:# stopt het
             print("Closed")
             exit()# sluit de class
        list()# begint het opnieuw
        exit()
        
def list():# functie voor vragen van command
    commands = int(input(f" 1) Spellen bekijken \n 2) Spel toevoegen \n 3) Totaalprijs berekenen \n 4) Afsluiten \n "))
    if commands <= 4:#als het ingevoerde nummer onder 5 is
        whishlisty = whishlist(commands)# variable voor de whishlist
        whishlisty.start(commands)# start de whishlist geeft de commands info over
    else:# als het boven 4 is
        print("ongeldige invoer \n")
     
list()


