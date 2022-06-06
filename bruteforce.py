import csv


class Action:
    def __init__(self, x):
        self.name = x[0]
        self.weight = int(x[1])
        self.roi = float(x[2])


skippedline = 0
actions_list = {}

with open("bourse.csv") as f:
    for line in f:
        if(skippedline >= 1):
            x = line.split(",")
            actions_list[x[0]] = Action(x)

        skippedline += 1

# print(type(actions_list['Action-7'].weight))
wallet = 500
combinaison = []

while wallet >= 500:
    for action in actions_list:
        print(action)
        for weight in action :
            weight = x.weight
            print(x[1])
            wallet - weight