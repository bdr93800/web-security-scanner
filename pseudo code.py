# Fonction main
1. Récupérer l'URL (argparse ou input)
2. Envoyer la requête GET → récupérer response (headers + cookies + HTML)
3. Appeler verif_headers(response.headers)
4. Appeler verif_cookies(response.cookies)
5. Parser le HTML avec BeautifulSoup
6. Pour chaque <form> trouvé → appeler verif_csrf(form)
7. Afficher le rapport final

# Fonction verif_headers(headers)
1. Vérifier la présence de :
   - Content-Security-Policy
   - X-Frame-Options
   - X-Content-Type-Options
   - Strict-Transport-Security
   - Referrer-Policy
   - Permissions-Policy
   - X-XSS-Protection
2. Pour chaque header manquant → ajouter à une liste "manquants"
3. Retourner la liste (plus utile qu'un simple True/False)

# Fonction verif_cookies(cookies)
1. Pour chaque cookie :
   - Vérifier flag Secure
   - Vérifier flag HttpOnly
   - Vérifier SameSite (Strict ou Lax)
2. Retourner un dict  {nom_cookie: [flags_manquants]}

# Fonction verif_csrf(form)
1. Récupérer tous les <input type="hidden"> du formulaire
2. Vérifier si un input a un nom qui ressemble à un token :
   - csrf, token, _token, authenticity_token, nonce...
3. Vérifier si method="GET" sur un formulaire (mauvaise pratique)
4. Retourner True (protégé) ou False (vulnérable) + raison