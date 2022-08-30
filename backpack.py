import time
from bruteforce import  Wallet
import tracemalloc



timer = time.time()
tracemalloc.start()

def backpack(dataset, max_weight):
    portfolio = Wallet(max_weight = max_weight)
  
    dataset = Wallet.load_actions(dataset_path="dataset1_Python+p7.csv")
    dataset.sort(key= lambda x: -x.profit)
    for action in dataset:
        try:
            portfolio.add(action)
        except:
            continue
    print(f"Le cout est de {portfolio.weight}€ pour un bénéfice de {portfolio.benefits}€, {portfolio.action_names}")


def main():
    max_weight = 500
    dataset = Wallet.load_actions(dataset_path="dataset1_Python+p7.csv")
    list_action = dataset.sort(key= lambda x: -x.profit)
    backpack(dataset = list_action, max_weight= max_weight)
    print(f"Exécuté en : {time.time() - timer} secondes")

    bytes_usage = tracemalloc.get_tracemalloc_memory()
    print(bytes_usage, "bytes utilisés pour l'exécution du programme.")
    tracemalloc.stop()

if __name__ == "__main__":
    main()


#librairie mémoire -> Tracemalloc
