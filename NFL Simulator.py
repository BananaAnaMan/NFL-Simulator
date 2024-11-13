class Sim_Drive:
    def __init__(self, team_one, team_two):
        match self.team_one:
            case "Arizona Cardinal":
                self.team_one = 76
            case "Atlanta Falcons":
                self.team_one = 84
            case "Baltimore Ravens":
                self.team_one = 90
            case "Buffalo Bills":
                self.team_one = 85
            case "Carolina Panthers":
                self.team_one = 79
            case "Chicago Bears":
                self.team_one = 81
            case "Cincinnati Bengals":
                self.team_one = 87
            #still a work in progress right now



    


class Sim_Game:
    def __init__(self):
        self.num_Drive = 12
