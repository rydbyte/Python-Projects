import spelonderdelen as parts#importeer module met alle onderdelen referring to it as parts
import os

call = False# variable boolean voor als iemand called

ja_nee = "2"#varaiable string voor het begin
while ja_nee != "1":#zo lang ja_nee niet de string 1 is leg de regels uit en vraagt om input dat de ja_nee verandert
    parts.rules()#functie van het spelonderdelen dat de regels print
    ja_nee = input("Begin spel? \n1.Ja\n2.Nee\n")

if ja_nee == "1":#als iemand als inut de string 1 zet dan begint het spel

    parts.deck_.start()#functie van module waardoor het start
    while call == False:#zolang call false is 
        hit_call = input("1.Hit\n2.Call\n")
        if hit_call ==  "1":#als cal 1 is
            parts.deck_.hit("player")#module voor een speler kaart geven
        if hit_call != "1" and not parts.player.players_hand:#als een speler probeert de callen maar er nog geen kaarten in zijn hand zitten
            print("Moet eerste kaart pakken")
        if hit_call != "1" and parts.player.players_hand:#als iemand called en wel kaarten hebt
            parts.deck_.end()#functie voor het eindigen
            exit()#sluit de code
            
