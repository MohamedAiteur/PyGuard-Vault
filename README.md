# 🛡️ PyGuard-Vault

Un gestionnaire de mots de passe léger, interactif et sécurisé en ligne de commande (CLI), développé en Python. Ce projet implémente un système de chiffrement symétrique pour stocker et restituer des identifiants de manière locale et partielle.

---

## 🔒 Fonctionnalités Cyber & Développement

*   **Chiffrement Symétrique AES-128 (Fernet) :** Utilisation de la bibliothèque `cryptography` pour garantir la confidentialité des données stockées. Chaque mot de passe est chiffré avant écriture sur le disque.
*   **Persistance des Données :** Stockage structuré des identifiants au sein d'un fichier plat `passwords.json`.
*   **Gestion Autonome des Clés :** Génération automatique d'une clé de sécurité locale (`secret.key`) si aucune clé valide n'est détectée au lancement.
*   **Séparation des Responsabilités (Clean Code) :** Code modulaire découpé en fonctions dédiées pour le chargement des clés, la lecture/écriture des fichiers et la logique applicative.
*   **Expérience Utilisateur Épurée :** Interface en ligne de commande interactive avec boucle de contrôle et normalisation des entrées utilisateur.

---

## 🛠️ Architecture du Projet

Le projet est structuré de façon à isoler la logique métier des secrets d'exécution :

*   `main.py` : Script principal contenant la logique du menu interactif et les opérations de chiffrement/déchiffrement.
*   `requirements.txt` : Liste des dépendances requises pour l'environnement d'exécution.
*   `.gitignore` : Configuration de sécurité interdisant le suivi et la publication des secrets locaux sur les dépôts distants.
*   `secret.key` *(Généré localement / Ignoré par Git)* : Clé cryptographique Fernet unique.
*   `passwords.json` *(Généré localement / Ignoré par Git)* : Base de données locale contenant les empreintes chiffrées.

---

## 🚀 Installation et Utilisation

### 1. Prérequis
Assurez-vous d'avoir Python 3.12+ installé sur votre système.

### 2. Cloner le projet et installer les dépendances
```bash
# Installez la bibliothèque cryptographique requise
pip install -r requirements.txt