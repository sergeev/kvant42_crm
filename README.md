## Уставнока приложения
#### Базовые команды


###### Создание приложения
````bash
python3 manage.py startapp
````

###### Миграции

````bash
python3 manage.py migrate
````
###### Обновить или добавить новые миграции НАЗВАНИЕ_МИГРАЦИИ
````bash
python3 manage.py makemigrations kvantums
python3 manage.py makemigrations personals
python3 manage.py makemigrations students
````

###### Создание админа

````bash
python3 manage.py createsuperuser
````

###### Запуск сервера
````bash
python3 manage.py runserver 
````