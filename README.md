# Веб-сайт на Flask & sqlite3 & scraping. <br/>Home work for UAI, lesson 17.

![alt-текст](https://github.com/HeyArtem/uai_lesson_17_Sqlite/blob/main/pictures/banner.png "Baner")

## Тех.детали:
* _Flask_
* _Flask-SQLAlchemy_
* _sqlite3_
* _flask_migrate_
* _Jinja2_
* _requests_
* _BeautifulSoup_
* _os_
* _json_
* _datetime_
<br/><br/>
<hr>


## Описание:
Сайт парсит данные с сайта www.proficosmetics.ru (раздел шампуни), сохраняет их в json. Json сохраняется в БД sqlite3. 

Пользователь имеет возможность самостоятельно (заполнив форму вручную) внести запись в БД. Пользователь может сортировать, обновлять, удалять данные в БД. 

Так же реализовал боковой слайдер (так же с возможностями сортировки)
<br/><br/>
<hr>


## Архитектура:
-  app.py<br/>
oсновной фаил, который нужно запускать [$ python app.py]

- data<br/>
директория (создается автоматически), парсер сохраняет собранную информацию (первую страницу и json c собранной информацей с сайта www.proficosmetics.ru)

- instance<br/>
директория с БД shampoo.db (создается автоматически)

- pictures<br/>
скриншоты для README

- static<br/>
директория со стилями

- templates<br/>
директория с html-страницами

- notes_uai_lesson_17_Sqlite<br/>
рабочие записи

- profcosmetics.py<br/>
скрипт с парсером, собирает данные с сайта www.proficosmetics.ru, сохряняет в директорию data
<br/><br/>
<hr>



## Особенности
Пользователь может:
* Парсинг - спарсить новые данные
* Обновить БД - перенести данные в БД
* Очистить БД - очистить БД. Спарсенный json не удаляется
* Добавить запись в БД - на странице с формой, ввести свои данные в БД
* Сортировка по (-id, -Цене, -Имени) - отсортировать данные

Боковой слайдер:
* Домашняя страница
* Очистить БД
* Сортировка по (-id, -Цене, -Имени, -Дате) - отсортировать данные
<br/><br/>
<hr>



## Примечание:
Html, css, div- с этим почти не работал. Сосредоточился на создании и работе с БД.<br/>
Можно было реализовать удаление отдельного поста, попробовать работать с картинками.
<br/><br/>
<hr>


## Что бы запустить проект:
- создать директорию на компьютере
- открыть нужный репозиторий-Code-HTTPS-скопировать ссылку
```
$ git clone +ссылка
```
- перейти в паку с проектом
- создать виртуальное окружение
```
$ python3 -m venv venv
```
- активировать виртуальное окружение 
```
$ source venv/bin/activate
``` 

```
$ pip install -U pip setuptools
``` 

- установить библиотеки из requirements.txt 
```
$ pip install -r requirements.txt 
```


- открыть проект в VS Code
```
$ code .
```

- Возможно потребуются свежие headers (www.proficosmetics.ru)
<br/><br/>
<hr>

![alt-текст](https://github.com/HeyArtem/uai_lesson_17_Sqlite/blob/main/pictures/Exemple%201.png "Exemple 1")
![alt-текст](https://github.com/HeyArtem/uai_lesson_17_Sqlite/blob/main/pictures/Exemple%202.png "Exemple 2")
![alt-текст](https://github.com/HeyArtem/uai_lesson_17_Sqlite/blob/main/pictures/Exemple%203.png "Exemple 3")
