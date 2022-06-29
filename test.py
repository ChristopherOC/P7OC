import csv
from dataclasses import dataclass
from importlib.resources import path
import itertools
import time


timer = time.time()

@dataclass
class Action:
    name: str
    weight: float
    profit: float

def convert_data(d: dict) -> dict:
    d["weight"] = float(d["weight"])
    d["profit"] = float(d["profit"])
    return d

def load_actions(dataset_path: str):
    with open(dataset_path) as f:
        return [Action(**convert_data(d)) for d in csv.DictReader(f)]



def main():
    dataset = load_actions(dataset_path="bourse.csv")
    max_weight = 500
    total_spent = 0
    full_list=[]
    final = []
    # print(sum(item.weight for item in dataset))
    # print(dataset)
    for i in range(len(dataset)+1):
        combination = itertools.combinations(dataset, i)
        full_list += list(combination)


    for combination in full_list:
        for item in combination:
            total_spent += item.weight
            
            if total_spent <= 500:
                final.append(item)
  
    print(final)
    print(total_spent)
    print(f"Exécuté en : {time.time() - timer} secondes")

if __name__ == "__main__":
    main()


# itertools.combinations   à implémenter pour le calcul de la forcebrute