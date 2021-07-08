# Repo entrainement pour les tests unitaires

## Table des matières

[[_TOC_]]

## Documentation

L'ensemble des concepts pour le langage Java sont présent à [la FAQ tests](https://java.developpez.com/faq/tests/) sur developpez.com.

## Pré-requis

Dans cette formation nous allons voir le concept des tests unitaires et des mocks à la fois pour Java mais aussi Python. La partie pratique sera faite avec Python.

Pour pouvoir suivre cette formation, il vous faudra les outils suivants sur votre machine:

* docker
* docker-compose
* git

## Tester l'api TODO

### Créer votre branche

Créer une branche git `main_{votre nom}` à partir de `main`.

### Tester l'application en local avec curl

Se référer à [cette documentation](./todoapi/README.md)

### Compléter les tests unitaires

* Compléter les tests en `TODO` dans le fichier `unit_tests/todoapi/tests/test_todo_repository.py`
* Assurez-vous qu'ils passent en vous référent à [cette documentation](./todoapi/README.md)
* Pushez votre branche régulièrement et observez le résultat sur le pipeline
