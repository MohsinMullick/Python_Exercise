class Team:
    team = ""
    player_name = ""

    def __init__(self, team, player_name):
        self.team = team
        self.player_name = player_name

    def display(self):
        print(f"Team: {self.team}, Player_Name: {self.player_name}")


team1 = Team('Barcelona', 'Raphinha')
team1.display()

team2=Team('Real_Madrid','Vinicius Junior')
team2.display()

team3=Team("Inter Milan","Marcus Thuram")
team3.display()

