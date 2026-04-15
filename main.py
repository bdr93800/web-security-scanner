import argparse
import requests
from bs4 import BeautifulSoup

from verif_header import verif_headers
from verif_cookies import verif_cookies
from verif_csrf import verif_csrf

def main():
    #  1. Récupérer l'URL
    parser = argparse.ArgumentParser(description="Mini scanner de sécurité web")
    parser.add_argument("url", help="URL cible à analyser")
    args = parser.parse_args()

    url = args.url

    #  2. Requête HTTP
    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException as e:
        print(f"[ERREUR] Requête impossible : {e}")
        return

    headers = response.headers
    set_cookie_headers = response.raw.headers.get_all("Set-Cookie") or []

    # parsing HTML
    html = response.text


    soup = BeautifulSoup(html, "html.parser")

    forms = soup.find_all("form")


    #  3. Analyse
    resultats_headers = verif_headers(headers)
    resultats_cookies = verif_cookies(set_cookie_headers)
    resultats_csrf = []

    for i, form in enumerate(forms, start=1):
        res = verif_csrf(form)
        resultats_csrf.append({
            "formulaire": i,
            "resultat": res
        })
    #  4. Rapport
    afficher_rapport(resultats_headers, resultats_cookies,resultats_csrf)


# =========================
# 📊 AFFICHAGE RAPPORT
# =========================

def afficher_rapport(headers, cookies, csrf):
    print("\n==============================")
    print("   RAPPORT DE SECURITE WEB   ")
    print("==============================\n")

    # 🔐 HEADERS
    print("---- HEADERS ----")
    for nom, info in headers.items():
        if info["statut"] == "ok":
            print(f"[OK] {nom}")
        elif info["statut"] == "manquant":
            print(f"[MANQUANT] {nom} -> {info['message']}")
        elif info["statut"] == "invalide":
            print(f"[INVALIDE] {nom} -> {info['valeur']} | attendu : {info['attendu']}")

    # 🍪 COOKIES
    print("\n---- COOKIES ----")
    if not cookies:
        print("[OK] Aucun problème détecté")
    else:
        for nom_cookie, problemes in cookies.items():
            if not problemes:
                print(f"[OK] {nom_cookie}")
            else:
                print(f"[COOKIE] {nom_cookie}")
                for p in problemes:
                    print(f"  - {p}")

   # CSRF
    print("\n---- CSRF ----")

    if not csrf:
        print("Aucun formulaire trouvé")
    else:
        for item in csrf:
            num = item["formulaire"]
            res = item["resultat"]

            if res["protege"]:
                print(f"[OK] Formulaire {num} -> {res['raison']}")
            else:
                print(f"[VULNERABLE] Formulaire {num} -> {res['raison']}")

    print("\n==============================\n")


# 🔹 Lancement
if __name__ == "__main__":
    main()