
import random

playersNameList = ["Hossein", "Maziar", "Akbar", "Nima", "Mahdi", "Farhad", "Mohammad", "Khashayar", "Milad", "Mostafa", "Amin", "Saeid", "Pooya", "Porya", "Reza", "Ali", "Behzad", "Soheil", "Behrooz", "Shahrooz", "Saman", "Mohsen"]

class Human():
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    
class Footballer(Human):
    def __init__(self, name, team =""):
        super().__init__(name)
        self.team = team
    def getTeam(self):
        return self.team
    def setTeam(self, team):
        self.team = team
        
team_A = []
team_B = []
playerObjectList = []
limit = int(len(playersNameList)/2)
    
for i in range(limit):
    randomPlayerName = random.choice(playersNameList)
    player = Footballer(randomPlayerName,"A")
    team_A.append(player.getName())
    playerObjectList.append(player)
    playersNameList.remove(randomPlayerName)


for i in range(limit):
    randomPlayerName = random.choice(playersNameList)
    player = Footballer(randomPlayerName,"B")
    team_B.append(player.getName())
    playerObjectList.append(player)
    playersNameList.remove(randomPlayerName)


print(f"team A:  {team_A}")
print(f"team B:  {team_B}")

print()
for i in range(len(playerObjectList)):
    print(f"{playerObjectList[i].getName()} team: {playerObjectList[i].getTeam()}")
