from flask import Flask, render_template, request, redirect
from data import data
import random
#import os
app = Flask(__name__)


# Создаем переменные с карточками
sherif_1 = 'Шериф'
sherif_2 = 'Шериф'
doctor = 'Доктор'
mir_1 = 'Мирный'
mir_2 = 'Мирный'
all_cards = [sherif_1, sherif_2, doctor, mir_1, mir_2]

# Маршрут для отображения шаблона и обработки формы
#def get_data():
#    with open('data.py', 'r', encoding="utf-8") as f:
#        data = f.read()
#    return data
@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            # Получаем выбранную карточку из формы
            player_card = request.form['card']
            # Выбираем случайным образом карточку компьютера
            computer_card = random.choice(all_cards)
            # Определяем победителя
            if len(data)<4: 
                return render_template('index.html'), 302
            else:
                if player_card == 'Мафия':
                     result = 'Вы проиграли! Компьютер выбрал карту ' + computer_card
                elif player_card == computer_card:
                    result = 'Ничья! Компьютер выбрал ту же карту: ' + computer_card
                else:
                    result = 'Вы выиграли! Компьютер выбрал карту ' + computer_card
                    # Возвращаем результат и обновляем страницу
                return render_template('index.html', result=result, data = data)
        else:
        # Если метод запроса GET, отображаем шаблон без результата
            return render_template('index.html', data = data)

    except KeyError:
        return render_template('error.html'), 400
    
@app.route('/delete_card', methods=['POST'])
def delete_card():
    id = request.form['id']
    for card in data:
        print (str(id) )
        if str(card['id']) == str(id):
            data.remove (card)
    return redirect ('/admin')


# пофиксить добавление карточки
@app.route('/add_player', methods=['POST'])
def add_ployer():
    pl = {}
    print(data)
    pl["id"] = random.randint(1, 1000)
    pl["player_role"] = request.form["player_role"]
    if len(data)>4: 
        return render_template('error.html'), 400
    else:
        data.append(pl)
#    writedata(f"data = {data}")
        return redirect('/admin')  
   

@app.route('/admin')
def admin():
    return render_template('admin.html', data=data)

if __name__ == '__main__':
    app.run (debug=True)
