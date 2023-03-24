
import threading
from fastapi import FastAPI

# Créer une instance de l'application FastAPI
app = FastAPI()

# Définir une route de test pour l'API
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Définir une fonction pour la boucle infinie
def infinite_loop():
    while True:
        print("I'm running in the background!")

# Créer deux threads pour exécuter la boucle infinie et l'API
t1 = threading.Thread(target=infinite_loop)
t2 = threading.Thread(target=app.run)

# Démarrer les threads
t1.start()
t2.start()

# Attendre que les threads se terminent (ce qui ne se produira jamais dans le cas de la boucle infinie)
t1.join()
t2.join()