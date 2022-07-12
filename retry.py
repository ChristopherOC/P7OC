import csv
from dataclasses import dataclass
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
    wallet = 0
    print(sum(item.weight for item in dataset))
    print(item.weight for item in dataset)
    # while wallet <= max_weight:
    #     wallet += (item.weight for item in dataset)
    # print(wallet)


    
    print(f"Exécuté en : {time.time() - timer} secondes")

if __name__ == "__main__":
    main()


# itertools.combinations   à implémenter pour le calcul de la forcebrute