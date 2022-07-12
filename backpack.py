import time
from bruteforce import load_actions, Action, Portfolio
import random



timer = time.time()

#trier par profit décroissant
#creer le portfolio
#Pour chaque action 
    #tenter ajouter l'action au portfolio
    # si échoue passer à l'action suivante 

    # retourner un portfolio dans le backpack 

def backpack(dataset):
    max_weight = 500
    dataset.sort(key = lambda x: -x.profit)
    print(dataset)
  


def main():
    max_weight = 500
    wallet = 0
    my_actions =[]
    dataset = load_actions(dataset_path="bourse.csv")
    
    
    backpack(dataset)

    print(f"Le cout est de {best_portfolio.weight}€ pour un bénéfice de {best_portfolio.benefits}€, {best_portfolio.action_names}")
    print(f"Exécuté en : {time.time() - timer} secondes")



if __name__ == "__main__":
    main()

    #recherche randrange