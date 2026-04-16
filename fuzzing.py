import requests
from concurrent.futures import ThreadPoolExecutor

# Fonction qui teste UNE seule URL
def tester_url(base_url, word):
    url = f"{base_url}/{word}"
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            print(f"[FOUND]    {url} → 200")
            return url
        elif response.status_code == 403:
            print(f"[FORBID]   {url} → 403")
            return url
        elif response.status_code in [301, 302]:
            print(f"[REDIRECT] {url} → {response.status_code}")
        elif response.status_code == 500:
            print(f"[ERROR]    {url} → 500")
            return url

    except requests.RequestException as e:
        print(f"[ERREUR] {url} : {e}")

    return None


# Fonction parente avec threads
def fuzzing(base_url, wordlist, threads=10):
    
    with ThreadPoolExecutor(max_workers=threads) as executor:
        resultats = executor.map(
            lambda word: tester_url(base_url, word),
            wordlist
        )

    # Filtrer les None
    pages_trouvees = [r for r in resultats if r]
    print("Les pages trouvées sont : ",  pages_trouvees)
    return pages_trouvees

