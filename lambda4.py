print('Lambdas Exercise')


signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
print(sorted(signups)) # Lexicographic sort
#write sorting by integer
key = lambda id : int(id[3:])
print(sorted(signups,key=key),'\n')


print(sorted(signups,key = lambda id : int(id[3:])))



print('Lambdas Exercise')

class Player:
   def __init__(self, name, score):
       self.name = name
       self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]


#Exercise: Sort this by score using lambda!
#write code here

# sort_lam = lambda Players: sorted(Players,key= lambda Player: Player.score,reverse=True)
# print(sort_lam(player_list))

player_list.sort(key = lambda players : players.score)
print([player.name for player in player_list])

