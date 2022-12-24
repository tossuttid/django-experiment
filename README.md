# Proyecto Final INFO2022

Vamos argentina!!!

Bueno, básicamente esto es una página para una fundación, que no creo que la quieran usar pq está muy verde, pero para aprobar anda joya.

Usamos sqlite en local (para evitar confusiones), y mysql en producción.

## Para correr la página por primera vez (en local)...

```
$ python venv .venv
$ source .venv

$ pip install -r requirements.txt

$python manage.py makemigrations
              ... migrate
              ... createadmin
              ... runserver

```

Se hizo esta rama, porque hubo que reescribir todo el proyecto, el otro solo funcionaba en local.
