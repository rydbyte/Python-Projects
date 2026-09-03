def nieuwe_som(ja_of_nee):# functie die begint met een nieuw som waarbij de info van ja_of_nee wordt meegenomen
    if ja_of_nee == "ja":#als ja_of_nee de str""ja" is dan
        bewerking()#begint met een som
    else:# als de str iets anders is dan "ja"
        print("gestopt")#pprint gestopt en vraagt niet meer om een nieuwe som

def opnieuw():# de opnieuw vraag functie
     ja_of_nee = input("Wil je een nieuwe berekening maken?: ")#vraagt om input str
     nieuwe_som(ja_of_nee)# start de funcite nieuw_som met de info van ja_of_nee

def som(type): # functie for berekening waarbij informatie wordt overgebracht wat dan typer wordt genoemd type = som_type
    getal1 = input("noem een getal: ")# vraagt om het eerste getal
    if type == "delen" and getal1 == "0":# speciaal voor delen als de som delen is, kan niet delen door 0 checkt voor dat
        print("error")#error
        opnieuw()# vraagt voor nieuwe berekening

    if getal1.isnumeric():# als het een nummer is dus geen letter
        print()# voor break line
        getal2 = input("noem het tweede getal: ")# vraagt om een tweede getal
        if type == "delen" and getal1 == "0":# check opnieuw ook het tweede getal voor 0 en delen
            print("error")#error
            opnieuw()#functie voor opnieuw
        if getal2.isnumeric():# checkt of getal nmr 2 ook een getal is geen letter 
           if type == "optellen": # als som_type/type string "optellen" is
            return float(getal1)+float(getal2)#float voor de string naar float zodat het berekent kan worden en returned de data als mijn_som
           elif type == "aftrekken":# als som_type/type string "aftrekken" is
            return float(getal1)-float(getal2) #float voor de string naar float zodat het berekent kan worden en returned de data als mijn_som
           elif type == "delen":# als som_type/type string "delen" is
            return float(getal1)/float(getal2)#float voor de string naar float zodat het berekent kan worden en returned de data als mijn_som
           elif type == "vermenigvuldigen":# als som_type/type string "vermendigvuldigen" is
            return float(getal1)*float(getal2)#float voor de string naar float zodat het berekent kan worden en returned de data als mijn_som
        else:
            print("error")
            opnieuw()
    else:
        print("error")
        opnieuw()

def bewerking(): # functie voor het starten van bewerking
    som_type = input("Welke bewerking wil je uitvoeren? (optellen, aftrekken, delen, vermenigvuldigen: ")# vraagt om input met de string als text som_type word wat is ingetypt
    if som_type == "delen" or som_type == "optellen" or som_type == "aftrekken" or som_type == "vermenigvuldigen": # checkt wat de string value is 
       mijn_som = som(som_type) # start de bereking functie waarbij de gekozen string value som_type word meegenomen als informatie mijn_som word wat word gereturned
       print(mijn_som) # print de berekening
       opnieuw()# start de functie voor het vragen van een nieuwe berekening
    else:# als het niet delen, optellen etc is dan error en vraagt of je een nieuwe berekening wilt maken
       print("error")
       opnieuw()# start de functie voor een nieuwe bewerking vragen
        