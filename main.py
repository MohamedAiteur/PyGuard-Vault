import os
import json
from cryptography.fernet import Fernet

# 1. Gestion de la clé de chiffrement
def charger_ou_creer_cle():
    if not os.path.exists("secret.key"):
        cle = Fernet.generate_key()
        with open("secret.key", "wb") as fichier_cle:
            fichier_cle.write(cle)
        print("🔑 Nouvelle clé de sécurité générée sous 'secret.key'.")
    else:
        with open("secret.key", "rb") as fichier_cle:
            cle = fichier_cle.read()
    return Fernet(cle)

# 2. Gestion du fichier JSON pour stocker les données
def charger_donnees():
    if not os.path.exists("passwords.json"):
        return {}
    with open("passwords.json", "r", encoding="utf-8") as fichier:
        try:
            return json.load(fichier)
        except json.JSONDecodeError:
            return {}

def sauvegarder_donnees(donnees):
    with open("passwords.json", "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, indent=4, ensure_ascii=False)

# 3. Programme principal avec le menu
def main():
    fernet = charger_ou_creer_cle()
    
    while True:
        print("\n" + "="*35)
        print("    🛡️  PYGUARD-VAULT - MENU  🛡️")
        print("="*35)
        print("1. Ajouter un nouveau mot de passe")
        print("2. Afficher un mot de passe")
        print("3. Quitter")
        print("="*35)
        
        choix = input("Choisissez une option (1-3) : ").strip()
        
        if choix == "1":
            service = input("\n🌐 Nom du service (ex: GitHub, Netflix) : ").strip()
            if not service:
                print("❌ Le nom du service ne peut pas être vide.")
                continue
                
            mdp_clair = input(f"🔑 Entrez le mot de passe pour {service} : ").strip()
            
            # Chiffrement (on convertit le texte en bytes, puis on chiffre)
            mdp_chiffre = fernet.encrypt(mdp_clair.encode()).decode()
            
            donnees = charger_donnees()
            donnees[service.lower()] = mdp_chiffre
            sauvegarder_donnees(donnees)
            
            print(f"✅ Mot de passe pour '{service}' chiffré et sauvegardé avec succès !")
            
        elif choix == "2":
            service = input("\n🔍 Quel service recherchez-vous ? : ").strip().lower()
            donnees = charger_donnees()
            
            if service in donnees:
                try:
                    # Déchiffrement (on récupère la chaîne, on la déchiffre, puis on décode en texte)
                    mdp_chiffre = donnees[service]
                    mdp_dechiffre = fernet.decrypt(mdp_chiffre.encode()).decode()
                    print(f"\n➔ Mot de passe trouvé : {mdp_dechiffre}")
                except Exception:
                    print("❌ Erreur lors du déchiffrement. La clé secrète est-elle correcte ?")
            else:
                print("❌ Aucun mot de passe enregistré pour ce service.")
                
        elif choix == "3":
            print("\n👋 Fermeture de PyGuard-Vault. Restez en sécurité !")
            break
        else:
            print("❌ Option invalide. Veuillez choisir 1, 2 ou 3.")

if __name__ == "__main__":
    main()