class Team:
        def __init__(self, name, skill):
            self.name = name
            self.skill = skill
            self.points = self.gf = self.ga = self.wins = self.draws = self.losses = 0

        def add_goals(self, goals):
            self.gf += goals