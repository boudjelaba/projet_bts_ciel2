# projet_bts_ciel2

![Python](https://img.shields.io/badge/python-3.11-blue)

![Docs](https://img.shields.io/badge/docs-complete-brightgreen)

![CI](https://github.com/boudjelaba/projet_bts_ciel2/actions/workflows/ci.yml/badge.svg)

## Objectifs

* Gérer un projet avec **GitHub (Issues, Projects, CI)**
* Faire le lien entre **informatique et réseaux**
* Planifier le travail et rédiger un **rapport**
* Utiliser **Git et GitHub correctement**
* Mettre en place des **tests automatiques (GitHub Actions)**

## Contenu du projet

- Task 1 – Python : prise en main
- Task 2 – Analyse de logs
- Task 3 – Test réseau
- Task 4 – BONUS : Mini serveur HTTP
- Diagramme de Gantt : `gantt.md`
- Rapport à compléter : `RAPPORT.md`

* Chaque tâche est indépendante.
* Lisez bien les consignes dans chaque fichier `.py`.

---

## Prérequis

- Python 3 installé
- Un terminal
- Un éditeur de code (VS Code recommandé)

Pour vérifier Python :
```bash
python --version
```

---

## Règles importantes

* Faites **au moins un commit par tâche**
* N’effacez pas les commentaires `# TODO`
* Respectez le **format des messages de commit**
* Ne modifiez **jamais** la version manuellement

---

## Format des messages de commit

Ce projet impose les **Conventional Commits**.

### Format attendu

```text
type(scope): description
```

### Types autorisés

* `feat` : nouvelle fonctionnalité
* `fix` : correction de bug
* `docs` : documentation
* `test` : tests
* `chore` : maintenance / nettoyage
* `ci` : configuration CI

### Exemples valides

```bash
git commit -m "feat(log): add log analyzer"
git commit -m "fix(ping): handle timeout"
git commit -m "docs: update README"
```

---

## Versioning automatique (semantic-release)

Ce projet utilise **semantic-release**.

| Type de commit    | Effet sur la version |
| ----------------- | -------------------- |
| `fix:`            | patch (x.y.**z**)    |
| `feat:`           | minor (x.**y**.0)    |
| `BREAKING CHANGE` | major (**x**.0.0)    |

> Le fichier `CHANGELOG.md` est mis à jour **uniquement lors d’une release automatique**.

---

## Installation de pre-commit (obligatoire)

À faire **une seule fois** sur votre machine :

```bash
pip install pre-commit
pre-commit install
```

> Après installation, Git refusera les commits mal formatés.

---

## Cas particuliers (TP)

### Commit sans impact version

```bash
git commit -m "docs: fix typo"
git commit -m "chore: update comments"
```

* Pas de release
* Pas de mise à jour du changelog

---

### Commit non conforme (à éviter)

```bash
git commit --no-verify -m "test"
```

Conséquences :

* le commit passe localement
* la CI accepte
* semantic-release **ignore le commit**
* ✖️ pas de changelog

---

## Déclenchement d’une release automatique

Le `CHANGELOG.md` est mis à jour **uniquement si TOUT est vrai** :

1. Commit conventionnel valide (`feat` ou `fix`)
2. Push sur la branche `main`
3. Tous les tests passent
4. semantic-release détecte un bump de version
5. Le job `release` s’exécute

---

## Vérification

### Historique Git

```bash
git log --oneline --decorate -5
```

Exemple :

```
chore(release): 1.2.0
```

### Tags

```bash
git tag
```

> `vX.Y.Z` récent = release réussie

---

## Releases GitHub

Dans l’onglet **Releases** :

* notes générées automatiquement
* contenu identique au `CHANGELOG.md`

> Le changelog n’est mis à jour **que lors d’une release automatique**,
> déclenchée par un commit `feat:` ou `fix:` poussé sur `main`.

---

## Github Projects

* **Backlog** : toutes les idées, fonctionnalités et tâches futures --> labels `idea`, `enhancement`
* **Todo** : tâches prêtes à être prises en charge --> labels `ready`, `bug`
* **In Progress** : travail en cours --> label `in-progress`
* **Review / Test** : PR ou code en revue / tests unitaires / validation --> label `review`, `testing`
* **Documentation** : tâches spécifiques doc, ou lien vers PR doc --> label `documentation`
* **Done** : tâches terminées et mergées --> label `done`

