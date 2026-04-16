import os
from colorama import Fore, Style, init
from main import scanner_site
from fuzzing import fuzzing

init(autoreset=True)

def afficher_menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(Fore.RED + """
 ██╗    ██╗███████╗██████╗      ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
 ██║    ██║██╔════╝██╔══██╗     ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
 ██║ █╗ ██║█████╗  ██████╔╝     ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
 ██║███╗██║██╔══╝  ██╔══██╗     ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
 ╚███╔███╔╝███████╗██████╔╝     ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
  ╚══╝╚══╝ ╚══════╝╚═════╝      ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
    """)

    print(Fore.WHITE + "=" * 65)
    print(Fore.YELLOW + "          🔒 Web Vulnerability Scanner v1.0")
    print(Fore.WHITE + "=" * 65 + "\n")

    options = [
        ("1", "🌐  Analyser un site",          "Headers, Cookies, CSRF"),
        ("2", "🔍  Fuzzing de répertoires",     "Découverte de pages cachées"),
        ("3", "💉  Test injection SQL",         "Error-based SQLi"),
        ("4", "⚡  Test XSS",                   "Reflected XSS"),
        ("5", "🗂️   Scan complet",              "Toutes les analyses"),
        ("0", "❌  Quitter",                     ""),
    ]

    for num, nom, description in options:
        if num == "0":
            print()
        print(
            Fore.CYAN  + f"  [{num}] " +
            Fore.WHITE + f"{nom:<30}" +
            Fore.BLACK + Style.BRIGHT + f"  {description}"
        )

    print(Fore.WHITE + "\n" + "=" * 65)
    return input(Fore.GREEN + "\n  Choix → " + Fore.WHITE)


def demander_url():
    return input(Fore.YELLOW + "\n  🎯 URL cible : " + Fore.WHITE)
import os

def demander_wordlist():
    fichier = input(Fore.GREEN + "\n  📂 Nom de la wordlist (ex: wordlist.txt) : " + Fore.WHITE)

    # Cherche dans le répertoire courant
    chemin = os.path.join(os.getcwd(), fichier)

    if not os.path.exists(chemin):
        print(Fore.RED + f"\n  ❌ Fichier '{fichier}' introuvable dans {os.getcwd()}")
        return None

    with open(chemin, "r") as f:
        wordlist = [ligne.strip() for ligne in f if ligne.strip()]

    print(Fore.GREEN + f"\n  ✅ {len(wordlist)} mots chargés depuis '{fichier}'")
    return wordlist



def lancer_menu():
    while True:
        choix = afficher_menu()

        if choix == "1":
            url = demander_url()
            scanner_site(url)

        elif choix == "2":
            url = demander_url()
            wordlist = demander_wordlist()
            #wordlist = ["login", "register", "admin", "dashboard"]
            fuzzing(url, wordlist)

        elif choix == "3":
            url = demander_url()
            print(Fore.YELLOW + "\n  [EN COURS] Test SQLi...")
            # test_sqli(url)

        elif choix == "4":
            url = demander_url()
            print(Fore.YELLOW + "\n  [EN COURS] Test XSS...")
            # test_xss(url)

        elif choix == "5":
            url = demander_url()
            print(Fore.YELLOW + "\n  [EN COURS] Scan complet...")
            scanner_site(url)
            fuzzing(url, ["login", "admin", "dashboard"])
            # test_sqli(url)
            # test_xss(url)

        elif choix == "0":
            print(Fore.RED + "\n  Au revoir !\n")
            break

        else:
            print(Fore.RED + "\n  ❌ Choix invalide")

        input(Fore.WHITE + "\n  Appuie sur Entrée pour revenir au menu...")


if __name__ == "__main__":
    lancer_menu()