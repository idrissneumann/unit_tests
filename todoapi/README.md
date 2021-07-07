# Todo API

Une api restful permettant de remplir une TODO List.

Cette API à l'origine viens de ce [repo github](https://github.com/paulodhiambo/flaskcrudapi) et a été ré-écrite pour fonctionner avec `docker` de manière portable et PostgreSQL au lieu de MySQL.

Elle a été modifiée afin d'être découpée en couche et rendre certaines choses mockables comme la connexion à la base de données par exemple.

## Table des matières

[[_TOC_]]

## Tester l'api en local

### Démarrer en local en utilisant docker

```shell
unit_tests/todoapi$ docker-compose up --force-recreate --build -d
```

### Vérifier la base de données

```shell
unit_tests/todoapi$ docker exec -u postgres -it todo_db psql todo -U todo
psql (9.4.26)
Type "help" for help.

todo=# \d
            List of relations
 Schema |     Name     |   Type   | Owner 
--------+--------------+----------+-------
 public | todos        | table    | todo
 public | todos_id_seq | sequence | todo
(2 rows)

todo=# \d todos
                                      Table "public.todos"
      Column      |          Type          |                     Modifiers                      
------------------+------------------------+----------------------------------------------------
 id               | integer                | not null default nextval('todos_id_seq'::regclass)
 title            | character varying(20)  | 
 todo_description | character varying(100) | 

todo=# SELECT * FROM todos;
 id | title | todo_description 
----+-------+------------------
(0 rows)
```

### Enregistrer une entrée via l'api

```shell
unit_tests/todoapi$ curl -X POST http://127.0.0.1:5000/api/v1/todo -H "Content-Type: application/json" -d '{"title":"une tâche", "todo_description":"une description de la tâche"}'
{"todo":{"id":1.0,"title":"une t\u00e2che","todo_description":"une description de la t\u00e2che"}}
```

=> Revérifier en bdd si un enregistrement a bien été ajouté

```shell
unit_tests/todoapi$ docker exec -u postgres -it todo_db psql todo -U todo
psql (9.4.26)
Type "help" for help.

todo=# SELECT * FROM todos WHERE id = 1;
 id |   title   |      todo_description       
----+-----------+-----------------------------
  1 | une tâche | une description de la tâche
(1 row)
```

### Modifier l'enregistrement via l'api

```shell
unit_tests/todoapi$ curl -X PUT http://127.0.0.1:5000/api/v1/todo/1 -H "Content-Type: application/json" -d '{"title":"la tâche"}'
{"todo":{"id":1.0,"title":"la t\u00e2che","todo_description":"une description de la t\u00e2che"}}
```

=> Revérifier en bdd si un enregistrement a bien été modifié

```shell
unit_tests/todoapi$ docker exec -u postgres -it todo_db psql todo -U todo
psql (9.4.26)
Type "help" for help.

todo=# SELECT * FROM todos WHERE id = 1;
 id |   title   |      todo_description       
----+-----------+-----------------------------
  1 | la tâche | une description de la tâche
(1 row)
```

### Récupérer l'enregistrement via l'API

```shell
unit_tests/todoapi$ curl -X GET http://127.0.0.1:5000/api/v1/todo/1
{"todo":{"id":1.0,"title":"la t\u00e2che","todo_description":"une description de la t\u00e2che"}}
```

### Supprimer l'enregistrement via l'API

```shell
unit_tests/todoapi$ curl -X DELETE http://127.0.0.1:5000/api/v1/todo/1
```

=> Revérifier en bdd si un enregistrement a bien été supprimé

```shell
unit_tests/todoapi$ docker exec -u postgres -it todo_db psql todo -U todo
psql (9.4.26)
Type "help" for help.

todo=# SELECT * FROM todos WHERE id = 1;
 id | title | todo_description 
----+-------+------------------
(0 rows)
```

### Récupérer tout les enregistements

```shell
unit_tests/todoapi$ curl -X GET http://127.0.0.1:5000/api/v1/todo
{"todos":[{"id":2.0,"title":"une t\u00e2che","todo_description":"une description de la t\u00e2che"},{"id":3.0,"title":"une autre t\u00e2che","todo_description":"une description de la t\u00e2che"}]}
```
