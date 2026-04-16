# 🔐 Web Security Scanner

Mini scanner de sécurité web développé en Python permettant d'identifier rapidement des **mauvaises configurations de sécurité côté client**.

---

## 🎯 Objectif

Ce projet a pour but de détecter automatiquement :

* 🔐 Headers de sécurité manquants ou mal configurés
* 🍪 Mauvaise configuration des cookies (Secure, HttpOnly, SameSite)
* 🛡️ Absence de protection CSRF dans les formulaires
* 🔍 Pages et répertoires cachés (fuzzing)

👉 Il s'agit d'un **outil éducatif**, inspiré du fonctionnement de scanners comme Burp Suite ou OWASP ZAP.

---

## ⚙️ Fonctionnalités

### 🔐 Analyse des headers HTTP
Vérifie la présence et la validité de :
* `Content-Security-Policy`
* `X-Frame-Options`
* `X-Content-Type-Options`
* `Strict-Transport-Security`
* `Referrer-Policy`
* `Permissions-Policy`
* `X-XSS-Protection`

---

### 🍪 Analyse des cookies
Pour chaque cookie détecté :
* Vérifie le flag `Secure`
* Vérifie le flag `HttpOnly`
* Analyse `SameSite` :
  * `Strict` / `Lax` → OK
  * `None` → ⚠️ plus risqué
  * absent → ❌ vulnérable

👉 Ignore automatiquement les cookies techniques (`AWSALB`, `AWSALBCORS`, etc.)

---

### 🛡️ Analyse CSRF
* Détection des formulaires HTML
* Vérification de la présence d'un token CSRF (`csrf`, `token`, `_token`, etc.)
* Détection des formulaires en `GET` (mauvaise pratique)

---

### 🔍 Fuzzing de répertoires
* Chargement d'une wordlist depuis le répertoire courant
* Test de chaque mot en parallèle via **multithreading**
* Détection par code HTTP :
  * `200` → page accessible
  * `403` → existe mais accès refusé
  * `301/302` → redirection
  * `500` → erreur serveur (peut révéler des infos)

---

## 🏗️ Architecture du projet

```bash
web-security-scanner/
│
├── launch.py            # Point d'entrée — menu interactif coloré
├── main.py              # Logique de scan (headers, cookies, CSRF)
├── verif_header.py      # Analyse des headers HTTP
├── verif_cookies.py     # Analyse des cookies
├── verif_csrf.py        # Analyse CSRF
├── fuzzing.py           # Fuzzing de répertoires (multithreading)
├── wordlist.txt         # Wordlist par défaut
├── requirements.txt     # Dépendances
└── README.md
```

---

## 🚀 Installation

### 1. Cloner le projet
```bash
git clone https://github.com/bdr93800/web-security-scanner.git
cd web-security-scanner
```

### 2. Créer un environnement virtuel (recommandé)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

---

## ▶️ Utilisation

```bash
python launch.py
```

Un menu interactif s'affiche :
<img width="935" height="416" alt="image" src="https://github.com/user-attachments/assets/b2b2cc36-c615-47e0-8b00-02fcaad56acb" />

---

## 📊 Exemple de sortie

```text
---- HEADERS ----
[OK] X-Frame-Options
[MANQUANT] Content-Security-Policy -> Empêche les injections XSS
[MANQUANT] Strict-Transport-Security -> Force HTTPS

---- COOKIES ----
[COOKIE] session
  - SameSite=None (moins protecteur contre CSRF)
[COOKIE] PHPSESSID
  - HttpOnly manquant
  - Secure manquant

---- CSRF ----
[VULNERABLE] Formulaire 1 -> Aucun token CSRF détecté

---- FUZZING ----
[FOUND]    https://site.com/admin → 200
[FORBID]   https://site.com/config → 403
[REDIRECT] https://site.com/login → 301
```

---

## ⚠️ Limites

Ce scanner est basé sur des **heuristiques** :
* Un token CSRF détecté ≠ protection garantie
* Une CSP présente ≠ configuration sécurisée
* Ne remplace pas un audit de sécurité complet

---

## 📚 Technologies utilisées

* Python 3
* `requests`
* `BeautifulSoup` (bs4)
* `colorama`
* `concurrent.futures` (multithreading)

---

## 🎓 Objectifs pédagogiques

Ce projet m'a permis de travailler sur :
* Parsing HTTP (headers, cookies bruts)
* Analyse de sécurité web (XSS, CSRF, Clickjacking)
* Parsing HTML avec BeautifulSoup
* Structuration d'un projet Python modulaire
* Multithreading avec `ThreadPoolExecutor`
* Interface CLI colorée avec `colorama`
* Utilisation de Git / GitHub

---

## 🔮 Améliorations prévues

* 💉 Test injection SQL (error-based)
* ⚡ Test XSS réfléchi
* 📊 Score global de sécurité ( /100)
* 📁 Export JSON / rapport HTML
* 🔍 Analyse plus poussée CSP / HSTS

---

## 🧪 Sites de test recommandés

| Site | Usage |
|---|---|
| `https://ginandjuice.shop` | Site vulnérable maintenu par PortSwigger |
| `https://the-internet.herokuapp.com` | Formulaires, auth, redirections |
| `http://localhost:3000` | OWASP Juice Shop en local (Docker) |

---

## ⚠️ Disclaimer

Ce projet est à but **éducatif uniquement**.
Ne pas utiliser sur des systèmes sans autorisation explicite.

---

## 👨‍💻 Auteur

Développé par **Badr**
Projet personnel en cybersécurité / pentesting
