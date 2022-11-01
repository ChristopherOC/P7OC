import csv

import sys
import itertools
import time
import tracemalloc


timer = time.time()
tracemalloc.start()
sys.setrecursionlimit(10000)

#Calcul les profits générés par les actions
class CalcProfit:
    def __init__(self, name, price, perc_benefits):
        self.name = name
        self.price = price
        self.perc_benefits = perc_benefits
        self.profit = self.calc_profit()
        
    def calc_profit(self):
        return self.price + self.price * (self.perc_benefits / 100)


    def __str__(self) -> str:
        return f"{self.name} - {self.profit}"

# Calcul les différentes combinaisons d'action possibles
class ListStock:
    def __init__(self, stock_list : list[CalcProfit]):
        self.stock = stock_list
        self.nb_action = len(self.stock)
        self.combination = self.get_combination(self.nb_action)
        self.best_combination = self.sorting_list()


    #Permet de créer les combinaisons d'actions
    def get_combination(self, nb_action, combination_list = []):
        if nb_action == 0:
            return combination_list
        else :
            combination_list.append(itertools.combinations(self.stock, nb_action))
            return self.get_combination(nb_action - 1, combination_list)

    #Permet de calculer le profit d'une liste d'action
    @staticmethod
    def calc_list_profit(combination_list):
        profit = 0
        for action in combination_list:
            profit += action.profit
        return profit

    #Permet de calculer le bénéfice généré par une liste d'action
    @staticmethod
    def calc_list_benefits(combination_list):
        benefits = 0
        for action in combination_list:
            benefits += action.perc_benefits
        return benefits

    #Tri les combinaisons afin de ne garder que la meilleure
    def sorting_list(self):
        best_profit = 0
        best_combination = []

        for combination_list in self.combination:
            for combination in combination_list:
                profit = self.calc_list_profit(combination)
                benefits = self.calc_list_profit(combination)
                if profit > best_profit and benefits:
                    best_combination = combination
                    best_profit = profit
        return best_combination

    def best_list(self):
        profit = round(self.calc_list_profit(self.best_combination), 2)
        benefits = round(self.calc_list_benefits(self.best_combination), 2)
        # name = (name for self.name in self.best_combination)
        return f"Voici la liste des actions :  pour un bénéfice de {benefits}, profit {profit}"

#Charge les actions stockés dans le fichier .CSV
data_reader = []
def load_actions(dataset_path : str):
    with open(dataset_path, "r") as f:
        read_csv = csv.reader(f)
        for row in read_csv :
            data_reader.append(CalcProfit(row[0], float(row[1]), float(row[2])))
    return data_reader


def main():
    dataset = load_actions(dataset_path= "bourse.csv")
    stock_list = ListStock(dataset)
    best_ = stock_list.best_list()
    print(best_)
    print(f"Exécuté en : {time.time() - timer} secondes")


if __name__ == "__main__":
    main()
    bytes_usage = tracemalloc.get_tracemalloc_memory()
    print(bytes_usage, "bytes utilisés pour l'exécution du programme.")
    tracemalloc.stop()


"sys.setrecursionlimit "
"Fonctionnel mais requiert des ajustements/ Temps d'exécution trop long / 2h sans résultat/ "