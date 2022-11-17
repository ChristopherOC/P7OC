import time
from bruteforce import  Wallet
import tracemalloc


timer = time.time()
tracemalloc.start()

#Création d'un "Sac-à-dos" pour tester les combinaisons
def backpack(dataset, max_weight):
    portfolio = Wallet(max_weight = max_weight) #Instanciation d'un portefeuille d'action
    dataset = Wallet.load_actions(dataset_path="dataset2_Python+P7.csv")
    dataset.sort(key= lambda x: -x.profit) #Trie les action par bénéfice de façon décroissante
    for action in dataset: #Boucle qui ajoute une action au portefeuille tant que le cout de 500€ n'est pas dépassé
        try:
            portfolio.add(action)
        except:
            continue
    print(f"Le cout est de {portfolio.weight}€ pour un bénéfice de {portfolio.benefits}€, {portfolio.action_names}")


def main():
    max_weight = 500
    dataset = Wallet.load_actions(dataset_path="dataset2_Python+P7.csv")
    list_action = dataset.sort(key= lambda x: -x.profit)
    backpack(dataset = list_action, max_weight= max_weight)
    print(f"Exécuté en : {time.time() - timer} secondes")

    bytes_usage = tracemalloc.get_tracemalloc_memory()
    print(bytes_usage, "bytes utilisés pour l'exécution du programme.")
    tracemalloc.stop()

if __name__ == "__main__":
    main()
