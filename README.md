# Repo entrainement pour les tests unitaires

## Table des matières

[[_TOC_]]

## Périmètre

Dans cette formation vous apprendrez à faire des tests unitaires et des mocks afin de bouchonner toutes vos dépendances externes que vous ne voulez pas tester dans le scope de vos TU avec les technologies suivantes :

* Java JUnit, AssertJ, Mockito
* Python Unittest

## Documentation

L'ensemble des concepts pour le langage Java sont présent à [la FAQ tests](https://java.developpez.com/faq/tests/) sur developpez.com.

Vous avez également les slides de la formation [ici](./slides_formation.pdf).

Vous avez aussi les vidéos de la formation disponibles sur youtube:
* [Partie 1](https://youtu.be/riikMWhuJGg)
* [Partie 2](https://youtu.be/4P0xjcOALjY)

## Dépôts de sources

* Repo principal : https://gitlab.comwork.io/comwork_training/unit_tests
* Miroir github : https://github.com/idrissneumann/unit_tests.git
* Miroir gitlab : https://gitlab.com/ineumann/unit_tests.git
* Miroir bitbucket : https://bitbucket.org/idrissneumann/unit_tests.git

## Pré-requis

Dans cette formation nous allons voir le concept des tests unitaires et des mocks à la fois pour Java mais aussi Python. La partie pratique sera faite avec Python.

Pour pouvoir suivre cette formation, il vous faudra les outils suivants sur votre machine:

* docker (>= 20.10.7)
* docker-compose (>= 1.29.2)
* git

## Tester l'api TODO

### Créer votre branche

Créer une branche git `main_{votre nom}` à partir de `main`.

### Tester l'application en local avec curl

Se référer à [cette documentation](./todoapi/README.md)

### Compléter les tests unitaires

* Compléter les tests en `TODO` dans le fichier [`unit_tests/todoapi/tests/test_app.py`](./todoapi/tests/test_app.py)
* Compléter les tests en `TODO` dans le fichier [`unit_tests/todoapi/tests/test_todo_repository.py`](./todoapi/tests/test_todo_repository.py)
* Assurez-vous qu'ils passent en vous référent à [cette documentation](./todoapi/README.md)
* Pushez votre branche régulièrement et observez le résultat sur le pipeline
