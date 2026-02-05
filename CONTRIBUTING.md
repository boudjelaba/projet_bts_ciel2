# Contribuer au projet BTS CIEL

Merci de votre intérêt pour ce projet pédagogique.
Ce document décrit les **règles et bonnes pratiques** pour contribuer correctement au dépôt.

## Objectif de ce document

* Garantir un code lisible et fonctionnel
* Harmoniser les contributions
* Assurer le bon fonctionnement de la CI et des releases automatiques
* Apprendre de **bonnes pratiques professionnelles**

## Prérequis

* Python **≥ 3.10**
* `pip`
* Git
* Un environnement Linux, macOS ou Windows
* Connaissances de base en Python et Git

## Installation pour contribuer

1. Forker le dépôt GitHub
2. Cloner le fork localement :

```bash
git clone https://github.com/boudjelaba/projet_bts_ciel.git
cd projet_bts_ciel
```

3. Installer les hooks Git (obligatoire) :

```bash
pip install pre-commit
pre-commit install
```

> Sans cette étape, les commits pourront être refusés plus tard par la CI.

## Bonnes pratiques de code

* Code Python clair, lisible et commenté
* Fonctions courtes et bien nommées
* Pas de dépendances inutiles
* Compatibilité Linux / macOS / Windows
* Respect des consignes présentes dans les fichiers (`# TODO`)

## Organisation du travail

* Toute contribution se fait **via une branche**
* La branche `main` est protégée

Créer une branche :

```bash
git checkout -b feature/ma-fonctionnalite
```

## Style des commits (obligatoire)

Ce projet utilise les **Conventional Commits**.
Tout commit non conforme sera **refusé automatiquement**.

### Format attendu

```text
type(scope): description courte
```

### Types autorisés

| Type    | Description                    |
| ------- | ------------------------------ |
| `feat`  | nouvelle fonctionnalité        |
| `fix`   | correction de bug              |
| `docs`  | documentation                  |
| `test`  | ajout ou modification de tests |
| `chore` | maintenance / nettoyage        |
| `ci`    | configuration CI               |

### Exemples valides

```text
feat(log): analyse des logs
fix(ping): corriger le timeout
docs: compléter le README
test: ajouter des tests unitaires
chore: nettoyer le code
ci: ajuster le workflow GitHub
```

## Versioning automatique (semantic-release)

Le versioning est **entièrement automatique**.

| Type de commit    | Impact sur la version |
| ----------------- | --------------------- |
| `fix:`            | patch (x.y.z)         |
| `feat:`           | minor (x.y.0)         |
| `BREAKING CHANGE` | major (x.0.0)         |

Les commits `docs`, `test`, `chore` et `ci` :

* ✔ sont acceptés
* ✖️ ne déclenchent **pas** de nouvelle version
* ✖️ ne mettent **pas** à jour le changelog

> **Ne modifiez jamais la version manuellement.**

## Changements cassants (BREAKING CHANGE)

Pour une rupture de compatibilité :

```text
feat!: refonte du projet
```

ou :

```text
feat(core): refonte du projet

BREAKING CHANGE: changement de structure du projet
```

## Intégration continue (CI)

Chaque **Pull Request** déclenche automatiquement :

* l’exécution des tests
* la vérification du format des commits
* les hooks pre-commit côté CI

> Le `CHANGELOG.md` est généré **uniquement** :

* lors d’un push sur la branche `main`
* après validation des tests
* si une nouvelle version est détectée

## Vérifications avant Pull Request

Avant d’ouvrir une PR, assurez-vous que :

* [ ] le code fonctionne
* [ ] les tests passent
* [ ] la CI est verte
* [ ] la documentation est mise à jour si nécessaire
* [ ] les commits respectent le format imposé

## Signaler un bug ou proposer une idée

* Ouvrir une **issue GitHub**
* Décrire clairement :

  * ce que vous faites
  * ce que vous attendez
  * ce qui se passe réellement
  * votre OS et la version de Python

## Code de conduite

Soyez pros.
Ce projet est aussi un **outil d’apprentissage**.

Merci pour vos contributions
