import json
import csv

def afficher_menu():
    print("===== MENU =====")
    print("""
1. Ajouter un nouvel enregistrement
2. Afficher toutes les données
3. Modifier un enregistrement
4. Supprimer un enregistrement
5. Sauvegarder (JSON / CSV / TXT)
6. Charger (JSON / CSV / TXT)
0. Quitter
""")

def ajouter_donnee(liste):
    el = {}
    el["id"] = int(input("ID : "))
    el["nom"] = input("Nom : ")
    el["age"] = int(input("Age : "))

    if el["id"] not in [e['id'] for e in liste]:
        liste.append(el)
        print(" Ajouté avec succès.")
    else:
        print("ID existe déjà !")

def afficher_donnees(liste):
    for e in liste:
        print(f"{e['id']} - {e['nom']} - {e['age']}")

def modifier_donnee(liste):
    ID = int(input("ID à modifier : "))
    for e in liste:
        if e["id"] == ID:
            e["nom"] = input("Nouveau nom : ")
            e["age"] = int(input("Nouvel âge : "))
            print(" Modifié.")
            return
    print(" Element non trouvé !")

def supprimer_donnee(liste):
    ID = int(input("ID à supprimer : "))
    for e in liste:
        if e["id"] == ID:
            liste.remove(e)
            print("Supprimé.")
            return
    print("Element non trouvé !")

def save_json(liste, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(liste, f, indent=4)

def save_csv(liste, filename):
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "nom", "age"])
        writer.writeheader()
        writer.writerows(liste)

def save_txt(liste, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for e in liste:
            f.write(f"{e['id']} - {e['nom']} - {e['age']}\n")

def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def load_csv(filename):
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # convertir age/id en int
        return [{ "id": int(r["id"]), "nom": r["nom"], "age": int(r["age"]) } for r in reader]

def load_txt(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lignes = f.readlines()
        liste = []
        for l in lignes:
            id_, nom, age = l.strip().split(" - ")
            liste.append({"id": int(id_), "nom": nom, "age": int(age)})
        return liste

def main():
    liste = []

    while True:
        afficher_menu()
        choix = input("Choix : ")

        if choix == "1":
            ajouter_donnee(liste)

        elif choix == "2":
            afficher_donnees(liste)

        elif choix == "3":
            modifier_donnee(liste)

        elif choix == "4":
            supprimer_donnee(liste)

        elif choix == "5":
            filename = input("Nom du fichier : ")
            ext = filename.split(".")[-1].lower()

            if ext == "json":
                save_json(liste, filename)
            elif ext == "csv":
                save_csv(liste, filename)
            elif ext == "txt":
                save_txt(liste, filename)
            else:
                print("Extension inconnue !")

        elif choix == "6":
            filename = input("Nom du fichier : ")
            ext = filename.split(".")[-1].lower()

            if ext == "json":
                liste = load_json(filename)
            elif ext == "csv":
                liste = load_csv(filename)
            elif ext == "txt":
                liste = load_txt(filename)
            else:
                print("Extension inconnue !")

        elif choix == "0":
            print("Quitter")
            break

        else:
            print(" Choix invalide !")