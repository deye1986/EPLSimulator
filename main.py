from math import factorial, exp
from random import random
from team import Team
from sys import stdout
from time import sleep


def type_writer(x): 
    '''apply a typewriter style graphic to the output in the terminal'''
    for char in str(x):
        sleep(0.01) # speed
        stdout.write(char) 
        stdout.flush()


def run_sim():
    '''Run English Premier League Sim'''
    higher = 1.148698355
    lower = 0.8705505633

    arsenal = Team("Arsenal", 79)
    aston_villa = Team("Aston Villa", 76)
    brighton = Team("Brighton and Hove Albion", 76)
    burnley = Team("Burnley", 76)
    chelsea = Team("Chelsea", 82)
    crystal_palace = Team("Crystal Palace", 77)
    everton = Team("Everton", 79)
    fulham = Team('Fulham', 74)
    leeds = Team('Leeds United', 78)
    leicester = Team("Leicester City", 79)
    liverpool = Team("Liverpool", 85)
    man_city = Team("Manchester City", 87)
    man_united = Team("Manchester United", 83)
    newcastle = Team("Newcastle United", 77)
    sheffield_united = Team("Sheffield United", 79)
    southampton = Team("Southampton", 76)
    tottenham = Team("Tottenham Hotspur", 81)
    westbrom = Team("West Brom", 73)
    west_ham = Team('West Ham United', 79)
    wolves = Team('Wolverhampton Wanderers', 78)


    teams = [arsenal,
            aston_villa, 
            brighton, 
            burnley, 
            chelsea,
            crystal_palace, 
            everton, 
            fulham, 
            leeds, 
            leicester, 
            liverpool, 
            man_city, 
            man_united,
            newcastle, 
            sheffield_united, 
            southampton, 
            tottenham, 
            westbrom,
            west_ham, 
            wolves]

    for team in teams:
        print(team.name, team.skill)


    def home_score(home, away):
        homeSkill = home.skill / 3
        awaySkill = away.skill / 3

        if homeSkill == awaySkill:
            raise ValueError

        if homeSkill > awaySkill:
            homeGoals = 0
            lambHome = higher ** (homeSkill - awaySkill)
            z = random()
            while z > 0:
                z = z - (((lambHome ** homeGoals) * exp(-1 * lambHome)) /
                         factorial(homeGoals))
                homeGoals += 1
            return (homeGoals - 1)

        if homeSkill < awaySkill:
            homeGoals = 0
            lambHome = higher ** (homeSkill - awaySkill)
            z = random()
            while z > 0:
                z = z - (((lambHome ** homeGoals) * exp(-1 * lambHome)) /
                         factorial(homeGoals))
                homeGoals += 1

            return (homeGoals - 1)

    def away_score(home, away):
        homeSkill = home.skill / 3
        awaySkill = away.skill / 3

        if homeSkill == awaySkill:
            return 'Teams cannot play themselves!'

        if awaySkill > homeSkill:
            awayGoals = 0
            lambAway = lower ** (homeSkill - awaySkill)
            x = random()
            while x > 0:
               x = x - (((lambAway ** awayGoals) * exp(-1 * lambAway)) /
                        factorial(awayGoals))
               awayGoals += 1
            return (awayGoals - 1)

        if awaySkill < homeSkill:
            awayGoals = 0
            lambAway = lower ** (homeSkill - awaySkill)
            x = random()
            while x > 0:
               x = x - (((lambAway ** awayGoals) * exp(-1 * lambAway)) /
                        factorial(awayGoals))
               awayGoals += 1
            return (awayGoals - 1)

    league_size = 20
    POINTS = []
    GOALS_FOR = []
    GOALS_AGAINST = []
    WINS =[]
    DRAWS = []
    LOSSES = []
    for x in range(league_size):
        POINTS += [0]
        GOALS_FOR += [0]
        GOALS_AGAINST += [0]
        WINS += [0]
        DRAWS += [0]
        LOSSES += [0]

    # PLAYING ALL TEAMS AGAINST EACH OTHER AND UPDATING STATISTICS
    for x in range(league_size):
        print("========================================")
        print(teams[x].name + "'s home games: ")
        print("========================================")
        for y in range(league_size):
            error = 0
            try:
                homeScore = home_score(teams[x], teams[y])
            except ValueError:
                pass
                error += 1
            try:
                awayScore = away_score(teams[x], teams[y])
            except ValueError:
                pass
            if error == 0:
                print(teams[x].name, homeScore, ":", awayScore, teams[y].name)
                GOALS_FOR[x] += homeScore
                GOALS_FOR[y] += awayScore
                GOALS_AGAINST[x] += awayScore
                GOALS_AGAINST[y] += homeScore
                if homeScore > awayScore:
                    WINS[x] += 1
                    LOSSES[y] += 1
                    POINTS[x] += 3
                elif homeScore == awayScore:
                    DRAWS[x] += 1
                    DRAWS[y] += 1
                    POINTS[x] += 1
                    POINTS[y] += 1
                else:
                    WINS[y] += 1
                    LOSSES[x] += 1
                    POINTS[y] += 3
            else:
                pass

    # ASSIGNING STATISTICS TO EACH TEAM
    for x in range(league_size):
        teams[x].points = POINTS[x]
        teams[x].gf = GOALS_FOR[x]
        teams[x].ga = GOALS_AGAINST[x]
        teams[x].wins = WINS[x]
        teams[x].draws = DRAWS[x]
        teams[x].losses = LOSSES[x]

    sorted_teams = sorted(teams, key=lambda t: t.points, reverse=True)


    print("| TEAM                      | POINTS | WINS | DRAWS | LOSSES | GOALS FOR | GOALS AGAINST |")
    for team in sorted_teams:
        print("|",team.name," "*(24 - len(team.name)),"|  ",team.points," "*(3 - len(str(team.points))),"| ",team.wins," "*(2 - len(str(team.wins))),"|  ",
              team.draws," "*(2 - len(str(team.draws))),"|  ",team.losses," "*(3 - len(str(team.losses))),"|    ",team.gf," "*(4 - len(str(team.gf))),"|     ",
              team.ga," "*(7 - len(str(team.ga))),"|")


run_sim()