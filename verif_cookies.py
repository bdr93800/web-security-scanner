import requests
from http.cookies import SimpleCookie

COOKIES_A_IGNORER = ["awsalb", "awsalbcors"]

def verif_cookies(set_cookie_headers):
    regles = {
        "secure": {
            "description": "Cookie transmis uniquement en HTTPS"
        },
        "httponly": {
            "description": "Cookie inaccessible via JavaScript (protège contre XSS)"
        },
        "samesite": {
            "description": "Protège contre le CSRF",
            "valeur_recommandee": "Lax"
        }
    }

    for header in set_cookie_headers:
        cookie = SimpleCookie()
        cookie.load(header)

        for nom, morsel in cookie.items():
            nom_lower = nom.lower()

            if nom_lower in COOKIES_A_IGNORER:
                continue

            print(f"\n[COOKIE] {nom}")
            print(f"Valeur : {morsel.value}")

            # 🔐 Secure
            if morsel["secure"]:
                print("[OK] Secure")
            else:
                print("[❌] Secure manquant -> Cookie envoyé en HTTP possible")

            # 🔐 HttpOnly
            if morsel["httponly"]:
                print("[OK] HttpOnly")
            else:
                print("[❌] HttpOnly manquant -> Accessible via JavaScript")

            # 🔐 SameSite
            samesite = morsel["samesite"]

            if not samesite:
                print("[⚠️] SameSite absent -> risque CSRF")
            elif samesite.lower() == "none":
                if morsel["secure"]:
                    print("[⚠️] SameSite=None (OK car Secure, mais plus risqué)")
                else:
                    print("[❌] SameSite=None sans Secure -> dangereux")
            elif samesite.lower() == "lax":
                print("[OK] SameSite=Lax")
            elif samesite.lower() == "strict":
                print("[OK] SameSite=Strict (très sécurisé)")
            else:
                print(f"[⚠️] SameSite inconnu : {samesite}")