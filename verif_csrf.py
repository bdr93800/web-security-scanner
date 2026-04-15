def verif_csrf(form):
    method = form.get("method", "get").lower()

    if method == "get":
        return {
            "protege": False,
            "raison": "formulaire en GET (mauvaise pratique)"
        }

    hidden_inputs = form.find_all("input", {"type": "hidden"})

    noms_tokens = ["csrf", "token", "_token", "authenticity_token", "nonce"]

    for inp in hidden_inputs:
        name = (inp.get("name") or "").lower()

        for token in noms_tokens:
            if token in name:
                return {
                    "protege": True,
                    "raison": f"token détecté : {name}"
                }

    return {
        "protege": False,
        "raison": "aucun token CSRF détecté"
    }