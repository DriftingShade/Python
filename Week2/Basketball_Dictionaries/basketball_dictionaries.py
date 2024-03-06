class Player:
    def __init__(self, player_info):
        self.name = player_info["name"]
        self.age = player_info["age"]
        self.position = player_info["position"]
        self.team = player_info["team"]
# Challenge 1 Update Constructor

players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics",
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers",
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers",
    },
    {
        "name": "Michael Jordan",
        "age": 60,
        "position": "Power Forward",
        "team": "Chicago Bulls",
    },
]

# Challenge 2: Creating instances using individual player dictionaries

kevin = {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets",
    }

jason = {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics",
    }

kyrie = {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets",
    }

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)


# Challenge 3: Make a list of Player instances from a list of dictionaries

player_instances = []

for player_info in players:
    player_instance = Player(player_info)
    player_instances.append(player_instance)

print(player_instances)