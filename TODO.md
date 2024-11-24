# TODO - Flipper (by gpt)

## 1. Initialisation du Projet
- [X] Installer Python (v3.9 ou supérieur).
- [X] Créer un environnement virtuel : `python -m venv venv`.
- [X] Activer l’environnement virtuel : `source venv/bin/activate` ou `venv\Scripts\activate`.
- [X] Installer les librairies nécessaires :
  - [ ] `requests`
  - [ ] `flask`
  - [ ] `pandas`
  - [ ] `schedule`
- [X] Créer la structure du projet :
/ ├── app.py ├── api_utils.py ├── data_processing.py ├── templates/ ├── static/ ├── requirements.txt

---

## 2. Intégration de l'API Albion Online Data Project
- [X] Lire la documentation de l'API Albion Online Data Project. (y'en a pas (bruh))
- [X] Identifier les endpoints nécessaires (exemple : `/prices/{item_id}`).
- [ ] Créer une fonction pour effectuer des appels API :
- [ ] Gérer les paramètres (item_id, villes, etc.).
- [ ] Gérer les erreurs d'API.
- [ ] Convertir les réponses JSON en données exploitables.

---

## 3. Traitement des Données
- [ ] Créer une fonction pour comparer les prix entre plusieurs marchés :
- [ ] Identifier les opportunités de profit (buy low, sell high).
- [ ] Filtrer les données non pertinentes (prix null, erreurs).
- [ ] Ajouter une fonctionnalité pour sauvegarder les données :
- [ ] Enregistrer dans un fichier CSV ou JSON.
- [ ] Utiliser **Pandas** pour structurer les données.

---

## 4. Création d'une API Backend avec Flask
- [ ] Configurer un serveur Flask minimal.
- [ ] Créer un endpoint pour récupérer les opportunités de profit :
- [ ] Endpoint : `/items/<item_id>`.
- [ ] Renvoyer les résultats en JSON.
- [ ] Tester le serveur localement : `http://127.0.0.1:5000/items/{item_id}`.

---

## 5. Automatisation
- [ ] Implémenter une fonction pour collecter les prix à intervalles réguliers.
- [ ] Utiliser la librairie `schedule` pour automatiser les appels API.
- [ ] Ajouter un script qui exécute ces tâches en arrière-plan.

---

## 6. Interface Utilisateur (optionnel)
- [ ] Créer une page HTML simple pour afficher les opportunités :
- [ ] Ajouter un tableau avec les colonnes suivantes :
  - ID de l'item
  - Ville de vente
  - Prix de vente
  - Ville d'achat
  - Prix d'achat
  - Profit potentiel
- [ ] Ajouter un script JavaScript pour appeler l’API Flask.
- [ ] Afficher dynamiquement les données dans le tableau.

---

## 7. Tests et Optimisation
- [ ] Tester avec différents items et marchés.
- [ ] Gérer les erreurs potentielles :
- Erreurs d’API (time-out, réponses incorrectes).
- Données manquantes ou corrompues.
- [ ] Optimiser les performances :
- Ajouter un cache pour réduire les appels API.
- Filtrer les données inutiles avant de les traiter.

---

## 8. Déploiement
- [ ] Héberger le backend sur une plateforme cloud (Heroku, Railway, etc.).
- [ ] Configurer un domaine ou une URL publique pour l’API.
- [ ] Héberger l’interface utilisateur (si nécessaire).

---

## Notes Additionnelles
- [ ] Vérifier que le projet respecte les conditions d’utilisation de l’API et du jeu.
- [ ] Documenter le projet pour faciliter la maintenance et l’ajout de nouvelles fonctionnalités.
