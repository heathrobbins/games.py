class Fun: 
  def __init__(self, name, players): 
    self.name = name
    self.players = players

list = []

list.append( Fun("Checkers", 2))
list.append( Fun("Chess", 2))
list.append( Fun("Scrabble", 3))

for obj in list:
    if obj.players == 3:
        print(obj.name,"is a", obj.players, "player game")

