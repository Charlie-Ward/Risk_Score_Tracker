InputMessage = ""
territories = {}
Players = []
AmountOfPlayers = int(input("How many players are playing: "))
for i in range(AmountOfPlayers):
    PlayerNumber = i + 1
    PlayerNumber = str(PlayerNumber)
    Players.append(input("Enter Player " + PlayerNumber + "'s name: "))

print("All Player's names are ", Players)
PNameCorrect = int(input("Correct: [0] - No, [1] - Yes: "))
if PNameCorrect == 0:
    print("Program Closing please restart")
    exit()
elif PNameCorrect == 1:
    print("Starting Game")
    AmountOfTerritories = int(input("How many territories are on your board: "))
    AmountOfTerritoriesperPlayerStart = AmountOfTerritories // AmountOfPlayers
    for player in Players:
        territories[player] = AmountOfTerritoriesperPlayerStart
    for player, num_territories in territories.items():
        print(f"{player} owns {num_territories} territories")
    AmountOfTerritoriesLeftOverAtStart = AmountOfTerritories % AmountOfPlayers
    for player in range (AmountOfTerritoriesLeftOverAtStart):
        territories[player] = territories[player] + 1
    for player, num_territories in territories.items():
        print(f"{player} owns {num_territories} territories")
else:
    print("Input Not Recognised")
    exit()