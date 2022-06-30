import csv
from dataclasses import dataclass
import itertools
import time
from typing import Sequence


timer = time.time()

@dataclass
class Action:
    name: str
    weight: float
    profit: float

    @property
    def benefits(self) -> float:
        return self.profit * self.weight / 100
    

class Portfolio:
    def __init__(self, max_weight: float, actions: Sequence[Action]):
        self.max_weight = max_weight
        self.actions = actions
        self.benefits = None
        if self.get_weight() > max_weight:
            raise Exception("Le cout des actions dépasse le cout maximum d'investissement pour ce portfolio")    
            
    
    def get_benefits(self) -> float:
        if self.benefits is None :
            self.benefits = sum(item.benefits for item in self.actions)
        return self.benefits
         

    def get_weight(self) -> float:
        return sum(item.weight for item in self.actions)
    

def convert_data(d: dict) -> dict:
    d["weight"] = float(d["weight"])
    d["profit"] = float(d["profit"])
    return d

def load_actions(dataset_path: str):
    with open(dataset_path) as f:
        return [Action(**convert_data(d)) for d in csv.DictReader(f)]

def get_combination(dataset):
    for repetition in range(1, len(dataset) + 1): #
        for combination in itertools.combinations(dataset, repetition):
            yield combination
        
    

def main():
    max_weight = 500
    print(f"Exécuté en : {time.time() - timer} secondes")
    # print(Portfolio(max_weight, load_actions("bourse.csv")))
    # print(f"Le profit est de {} pour un prix de {} avec les actions suivantes {}")
  
    dataset = load_actions(dataset_path="bourse.csv")
    max_weight = 500
    best_portfolio = None
    for action_list in get_combination(dataset):
        try:
            portfolio = Portfolio(max_weight=max_weight, actions=action_list)
        except:
            continue

        weight = sum(item.weight for item in portfolio)
        if weight > max_weight:
            continue
        profit = sum(item.profit for item in portfolio)
        if best_portfolio is None or (best_portfolio and best_profit < profit):
            best_portfolio = portfolio
            best_profit = profit
            best_weight = weight



if __name__ == "__main__":
    main()

