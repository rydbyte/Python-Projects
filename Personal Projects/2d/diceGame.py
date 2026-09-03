import random, time, os, sys

# Vars
dicePick = "Single"
playing = False
currentRoll = {"P1": 0, "P2": 0}
totalPoints = {"P1": 0, "P2": 0}

# Classes
class Player():
    def __init__(self, hearts, points):
        self.hearts = hearts
        self.points = points

# Functions
def PickGM():
    while True:
        GM = input(
            "(Press 1/2/3) Pick an option!\n"
            "1. P1 vs Comp\n"
            "2. P1 vs P2\n"
            "3. View Highscore\n"
        )
        if GM in ("1", "2", "3"):
            return GM
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

def InsertName(gm):
    P1Name = ""
    P2Name = ""
    if gm == "1":
        while P1Name == "":
            P1Name = input("Name P1: ")
            if P1Name != "":
                return P1Name
    else:
        while P1Name == "" or P2Name == "":
            P1Name = input("Name P1: ")
            P2Name = input("Name P2: ")
            if P1Name != "" and P2Name != "":
                return P1Name, P2Name

def PickRoll():
    while True:
        Pick = input("Pick a Roll Type:\n 1 = Single\n 2 = Double\n")
        if Pick == "1":
            print("Player picked single!")
            return "1"
        elif Pick == "2":
            print("Player picked double!")
            return "2"
        else:
            print("Invalid input! Please type 1 or 2.")

def Roll(Picked, Plr):
    # FIX: No more resetting both rolls here
    if Picked == "1":
        D6 = random.randint(1, 6)
        print(f"Rolled a {D6}!")
        currentRoll[Plr] = D6
        totalPoints[Plr] += D6

    elif Picked == "2":
        D6 = random.randint(1, 6)
        SD6 = random.randint(1, 6)
        print(f"Rolled a {D6}! Rolled a {SD6}! Total = {(SD6 + D6) / 2}")
        currentRoll[Plr] = (SD6 + D6) / 2
        totalPoints[Plr] += (SD6 + D6) / 2

def load_highscore():
    try:
        with open("highscore.txt", "r") as f:
            line = f.read().strip()
            if ":" in line:
                name, score = line.split(":", 1)
                return int(score), name
            else:
                return int(line), "Unknown"
    except FileNotFoundError:
        return 0, "None"
    except ValueError:
        return 0, "None"

def save_highscore(name, score):
    with open("highscore.txt", "w") as f:
        f.write(f"{name}:{score}")

# Main
print("Hello Player(s)!")

GM = PickGM()

if GM == "3":
    highscore, highscore_name = load_highscore()
    print("\n=== CURRENT HIGHSCORE ===")
    print(f"Highscore: {highscore}")
    print(f"By: {highscore_name}")
    print("=========================\n")
    GM = PickGM()

if GM == "1":
    P1Name = InsertName(gm=GM)
    P2Name = "Computer"
else:
    P1Name, P2Name = InsertName(gm=GM)

P1 = Player(3, 0)
P2 = Player(3, 0)

print(f"Dice battle!\n {P1Name} vs {P2Name}.")
playing = True

while playing:
    # FIX: Reset rolls ONCE per round
    currentRoll["P1"] = 0
    currentRoll["P2"] = 0

    print(f"{P1Name}'s Turn!", end=" ")
    time.sleep(1.3)
    print("❤️" * P1.hearts)
    time.sleep(1.3)
    Picked = PickRoll()
    time.sleep(1.3)
    Roll(Picked=Picked, Plr="P1")

    if GM == "1":
        int_ = random.randint(1, 2)
        comp_pick = str(int_)
        if comp_pick == "1":
            print("Computer picked single!")
        else:
            print("Computer picked double!")
        time.sleep(1.3)
        Roll(comp_pick, "P2")
    else:
        time.sleep(1.3)
        print(f"{P2Name}'s Turn!", end=" ")
        time.sleep(1.3)
        print("❤️" * P2.hearts)
        Picked = PickRoll()
        Roll(Picked=Picked, Plr="P2")

    # Compare rolls correctly
    if currentRoll["P1"] > currentRoll["P2"]:
        print(f"{P1Name} scored higher than {P2Name}!\n {P2Name} Lost a heart!")
        P2.hearts -= 1
        if P2.hearts <= 0:
            print(f"{P1Name} won!")
            print(f"Total points {P1Name}:\n {totalPoints['P1']}\nTotal points {P2Name}:\n {totalPoints['P2']}")
            winner_name = P1Name
            winner_score = totalPoints["P1"]
            highscore, highscore_name = load_highscore()
            if winner_score > highscore:
                print(f"🎉 NEW HIGHSCORE! {winner_name} set a new record with {winner_score} points!")
                save_highscore(winner_name, winner_score)
            else:
                print(f"Current highscore: {highscore} by {highscore_name}")
            playing = False

    elif currentRoll["P1"] < currentRoll["P2"]:
        print(f"{P2Name} scored higher than {P1Name}!\n {P1Name} Lost a heart!")
        P1.hearts -= 1
        if P1.hearts <= 0:
            print(f"{P2Name} won!")
            print(f"Total points {P1Name}:\n {totalPoints['P1']}\nTotal points {P2Name}:\n {totalPoints['P2']}")
            winner_name = P2Name
            winner_score = totalPoints["P2"]
            highscore, highscore_name = load_highscore()
            if winner_score > highscore:
                print(f"🎉 NEW HIGHSCORE! {winner_name} set a new record with {winner_score} points!")
                save_highscore(winner_name, winner_score)
            else:
                print(f"Current highscore: {highscore} by {highscore_name}")
            playing = False

    else:
        print("It's a draw!\nNo Players lose a heart.")
    
    time.sleep(2)
    os.system("cls")
