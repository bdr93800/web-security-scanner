import requests
# Vérification du headers
def verif_headers(headers):
    regles = {
        "Content-Security-Policy": {
            "description": "Empêche les injections XSS en limitant les sources autorisées",
            "valeurs_valides": None
        },
        "X-Frame-Options": {
            "description": "Protège contre le clickjacking",
            "valeurs_valides": ["DENY", "SAMEORIGIN"]
        },
        "X-Content-Type-Options": {
            "description": "Empêche le MIME sniffing",
            "valeurs_valides": ["nosniff"]
        },
        "Strict-Transport-Security": {
            "description": "Force HTTPS (HSTS)",
            "valeurs_valides": None
        },
        "Referrer-Policy": {
            "description": "Contrôle les infos envoyées dans le header Referer",
            "valeurs_valides": None
        },
        "Permissions-Policy": {
            "description": "Restreint l'accès aux APIs du navigateur",
            "valeurs_valides": None
        },
        "X-XSS-Protection": {
            "description": "Protection XSS pour anciens navigateurs",
            "valeurs_valides": ["1", "1; mode=block"]
        }
    }

    resultats = {}

    for nom_header, infos in regles.items():
        if nom_header not in headers:
            resultats[nom_header] = {
                "statut": "manquant",
                "message": infos["description"]
            }
            continue

        valeur = headers[nom_header]
        valeurs_valides = infos["valeurs_valides"]

        if valeurs_valides is None:
            resultats[nom_header] = {
                "statut": "ok",
                "valeur": valeur
            }
        elif valeur in valeurs_valides:
            resultats[nom_header] = {
                "statut": "ok",
                "valeur": valeur
            }
        else:
            resultats[nom_header] = {
                "statut": "invalide",
                "valeur": valeur,
                "attendu": valeurs_valides
            }

    return resultats

