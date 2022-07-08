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
        self.__max_weight = max_weight
        self.__actions = actions
        self.__benefits = None
        if self.weight > max_weight:
            raise Exception("Le cout des actions dépasse le cout maximum d'investissement pour ce portfolio")
    
    @property
    def action_names(self):
        return "|".join(action.name for action in self.__actions)
     
    def __gt__(self, other):
        if other is None:
            return True
        return self.benefits > other.benefits
    
    @property
    def benefits(self) -> float:
        if self.__benefits is None :
            self.__benefits = sum(item.benefits for item in self.__actions)
        return self.__benefits   

    @property
    def weight(self) -> float:
        return sum(item.weight for item in self.__actions)
    

def convert_data(d: dict) -> dict:
    d["weight"] = float(d["weight"])
    d["profit"] = float(d["profit"])
    return d

def load_actions(dataset_path: str):
    with open(dataset_path) as f:
        return [Action(**convert_data(d)) for d in csv.DictReader(f)]

def get_combination(dataset):
    for repetition in range(1, len(dataset) + 1): 
        for combination in itertools.combinations(dataset, repetition):
            yield combination

def main():
    dataset = load_actions(dataset_path="bourse.csv")
    max_weight = 500
    best_portfolio = None
    for action_list in get_combination(dataset):
        try:
            portfolio = Portfolio(max_weight=max_weight, actions=action_list)
        except:
            continue
        
        best_portfolio = max(best_portfolio, portfolio)
        
    print(f"Le cout est de {best_portfolio.weight}€ pour un bénéfice de {best_portfolio.benefits}€, {best_portfolio.action_names}")
    print(f"Exécuté en : {time.time() - timer} secondes")

if __name__ == "__main__":
    main()

