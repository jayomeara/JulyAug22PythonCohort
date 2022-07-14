players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

class Player:
    def __init__(self, list):
        self.name = "name"
        self.age = "age"
        self.position = "position"
        self.team = "team"
    @classmethod
    def add_players(cls, list):
        player_objects = []
        for dict in list:
            player_objects.append(cls(list))
        print(player_objects)
        return player_objects




kevin = players[0]
jason = players[1]
kyrie = players[2]
damien = players [3]
joel = players[4]
player1 = players[5]

print(kevin)
print(joel)