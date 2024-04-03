  Налаштування проєкту
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install Flask

  Для запуску програми локально
$ python app.py

  Bash-скрипт для розгортання на сервері
$ docker build -t flask-todo-master
$ docker run -p 4000:4000 -d flask-todo-master 
