# 🔐 Web Security Scanner

Mini scanner de sécurité web développé en Python permettant d’identifier rapidement des **mauvaises configurations de sécurité côté client**.

---

## 🎯 Objectif

Ce projet a pour but de détecter automatiquement :

* 🔐 Headers de sécurité manquants ou mal configurés
* 🍪 Mauvaise configuration des cookies (Secure, HttpOnly, SameSite)
* 🛡️ Absence de protection CSRF dans les formulaires

👉 Il s’agit d’un **outil éducatif**, inspiré du fonctionnement de scanners comme Burp Suite ou OWASP ZAP.

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

👉 Ignore automatiquement les cookies techniques (`AWSALB`, etc.)

---

### 🛡️ Analyse CSRF

* Détection des formulaires HTML
* Vérification de la présence d’un token CSRF (`csrf`, `token`, `_token`, etc.)
* Détection des formulaires en `GET` (mauvaise pratique)

---

## 🏗️ Architecture du projet

```bash
web-security-scanner/
│
├── main.py              # Point d’entrée (orchestration)
├── verif_header.py      # Analyse des headers
├── verif_cookies.py     # Analyse des cookies
├── verif_csrf.py        # Analyse CSRF
├── requirements.txt     # Dépendances
└── README.md
```

---

## 🚀 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/TON_USERNAME/web-security-scanner.git
cd web-security-scanner
```

---

### 2. Créer un environnement virtuel (recommandé)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## ▶️ Utilisation

```bash
python main.py https://example.com
```

---

## 📊 Exemple de sortie

```text
---- HEADERS ----
[OK] X-Frame-Options
[MANQUANT] Content-Security-Policy -> Empêche les injections XSS

---- COOKIES ----
[COOKIE] session
  - SameSite=None (moins protecteur contre CSRF)

---- CSRF ----
[VULNERABLE] Formulaire 1 -> aucun token CSRF détecté
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
* requests
* BeautifulSoup (bs4)

---

## 🎓 Objectifs pédagogiques

Ce projet m’a permis de travailler sur :

* Parsing HTTP (headers, cookies)
* Analyse de sécurité web (XSS, CSRF, Clickjacking)
* Parsing HTML avec BeautifulSoup
* Structuration d’un projet Python modulaire
* Utilisation de Git / GitHub

---

## 🔮 Améliorations possibles

* 📊 Score global de sécurité (ex: /100)
* 🎨 Sortie colorée (CLI)
* 📁 Export JSON / rapport PDF
* 🔍 Analyse plus poussée CSP / HSTS
* 🌐 Scan multi-pages

---

## ⚠️ Disclaimer

Ce projet est à but **éducatif uniquement**.
Ne pas utiliser sur des systèmes sans autorisation.

---

## 👨‍💻 Auteur

Développé par **Badr**
Projet personnel en cybersécurité / pentesting

---
