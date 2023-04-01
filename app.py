from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlite3
from datetime import datetime
import sqlite3
import json
from profcosmetics import get_data


# Создал приложение
app = Flask(__name__)

# Тип и имя БД
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shampoo.db"

# ???????
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Описываю таблицу
class Shampoo(db.Model):

    # Имя таблицы
    __tablename__ = "Shampoo"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, index=True)
    description = db.Column(db.String(120))
    price = db.Column(db.Integer)
    created = db.Column(db.String(30))

    # Используется когда несколько таблиц
    def __init__(self, name, description, price, created):
        self.name = name
        self.description = description
        self.price = price
        self.created = created
    
    def __repr__(self):
        return f"name: {self.name} \ndescription: {self.description}"


# Главная страница, сюда вывожу результаты
@app.route("/")
def index():
    info = Shampoo.query.all()
    
    print(f"Метод __repr__: {Shampoo.__repr__(Shampoo)}")

    return render_template("shampoo.html", list=info)


# Ввод данных в БД от пользователя
@app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        price = request.form["price"]              
        created = request.form["created"]

        # print("  created:", request.form["created"])

        # В переменную сохраняю текущую дату, что бы вставить если пользователь не введет свою дату
        now = datetime.now()

        # Если пользователь ввел дату, запишется дата от пользователя
        if request.form["created"]:
            created = request.form["created"]
            
        # Если пользователь не ввел дату, автоматически запишется текущая дата
        else:
            created = now.strftime("%Y-%m-%d")       

        # Сохраняю информацию для БД в переменную
        info = Shampoo(name=name, description=description, price=price, created=created)
        
        # Записываю инфу в БД, перенаправляю и вывожу содержимое БД на главной странице 
        try:
            db.session.add(info)
            db.session.commit()
            
            return redirect("/")
        
        except:
            return "Ошибка ввода данных"
        
        # finally:
        #     connection.close()
        #     return redirect("/")
    
    else:
        return render_template("create.html")
    

# Кнопка очиски БД 
@app.route("/del_db")
def delete_db():
    try:
        connection = sqlite3.connect("instance/shampoo.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM shampoo;")
        connection.commit()


    except Exception as ex:
        print("Oшибка записи данных")
    
    finally:
        connection.close()
        return redirect("/")   
    

# Чтение спарсенного json в БД
@app.route("/json_read")
def json_read():    

    # Сюда сохраню спарсенные данные из json
    data = []

    try:
        # Создаю соединение с БД
        connection = sqlite3.connect("instance/shampoo.db")

        # Создаю курсор
        cursor = connection.cursor()

        # Удаляю старую информацию в БД
        cursor.execute("DELETE FROM shampoo;")

        # Читаю json в переменную
        with open("data/all_data.json", encoding="utf8") as f:            
            data = json.load(f)

        # # В переменную сохраняю текущую дату
        # now = datetime.now()        
        
        # Записываю в БД, сохраненные из json данные
        for item in data:
            cursor.execute("INSERT OR REPLACE INTO shampoo(name, description, price, created) VALUES (?, ?, ?, ?)", 
                (
                item["card_name"],
                item["card_description"],
                item["card_price"],
                item["current_data"]
                # now.strftime("%Y-%m-%d")
                )
            )
        
        connection.commit()

    except Exception as ex:
        print(ex)

    # Закрываю БД Обязательно!, перенаправляю на главную страниницу
    finally:
        # print(f"data: {data}")
        connection.close()
        return redirect("/")


# Сортировка по ID по убыванию
@app.route("/sort_by_id")
def sort_by_id():
    info = Shampoo.query.order_by(Shampoo.id.desc()).all()

    return render_template("shampoo.html", list=info)


# Сортировка по имени
@app.route("/sort_by_name")
def sort_by_name():
    info = Shampoo.query.order_by(Shampoo.name).all()

    return render_template("shampoo.html", list=info)


# Сортировка по стоимости
@app.route("/sort_by_price")
def sort_by_price():
    info = Shampoo.query.order_by(Shampoo.price).all()

    return render_template("shampoo.html", list=info)


# Сортировка по Дате
@app.route("/sort_by_date")
def sort_by_date():
    info = Shampoo.query.order_by(Shampoo.created).all()

    return render_template("shampoo.html", list=info)


# Сортировка по id > 50. Не реализованиа в html
@app.route("/sort_id_dg")
def sort_id_dg():
    info = Shampoo.query.filter(Shampoo.id > 50).all()
    
    return render_template("shampoo.html", list=info)


# Страница с запуском парсера
@app.route("/new_json")
def new_json():    
    return render_template("new_json.html")


# Запуск парсера cайта www.proficosmetics.ru
@app.route("/start_parsing")
def start_parsing():
    x = get_data()
    return render_template("parsing_result.html", info=x)
    


if __name__ == "__main__":
    app.run(debug=True)
