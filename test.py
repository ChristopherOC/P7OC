import csv


class Action:
    def init(self, actions):
        self.name = actions[0]
        self.weight = int(actions[1])
        self.roi = float(actions[2])


actions_list = {}

with open('bourse.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)

    for line in f_csv:
        actions_list[line[0]] = Action(line)


# print(type(actions_list['Action-7'].weight))
wallet = 500
combinaison = []

for action in actions_list.values():
    weight = action.weight
    wallet = wallet - weight
    combinaison.append(action.name+':'+str(action.weight))

    if wallet <= 0 or wallet - weight <= 0:
        break

print(combinaison)