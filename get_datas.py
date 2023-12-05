import requests
import json

def fetch_sneakers(page):
    base_url = "http://54.37.12.181:1337/api/sneakers/"
    params = {"pagination[page]": page, 'pagination[pageSize]': 100}

    try:
        response = requests.get(base_url, params=params)

        # Vérifiez le statut de la réponse
        if response.status_code == 200:
            sneakers_data = response.json()
            # Vérifiez si les données de la page sont vides
            if len(sneakers_data["data"]) == 0:
                print(f"Aucune donnée sur la page {page}. Arrêt de la récupération.")
                return None
            # Traitez les données ici, par exemple, imprimez-les
            print(f"Page {page}: {sneakers_data}")
            return sneakers_data
        else:
            print(f"Erreur lors de la récupération des données de la page {page}. Statut code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as err:
        print(f"Erreur lors de la récupération des données de la page {page}: {err}")
        return None

def fetch_all_sneakers():
    all_sneakers_data = []
    page = 1
    while True:
        sneakers_data = fetch_sneakers(page)
        if sneakers_data == None:
            break
        all_sneakers_data.extend(sneakers_data["data"])
        page += 1

    return all_sneakers_data

def write_to_json(data, filename='data.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

# Appel de la fonction pour récupérer toutes les données
all_sneakers_data = fetch_all_sneakers()

# Écriture de toutes les données dans un fichier JSON
write_to_json(all_sneakers_data)