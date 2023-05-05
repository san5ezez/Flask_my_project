from flask import Flask, render_template, request, redirect
from data import data
import random
#import os
app = Flask(__name__)

import cgi

# Получаем данные из HTML формы
form = cgi.FieldStorage()
angle = form.getvalue("angle")

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
    #try:
        if request.method == 'POST':
            result = ''
            if len(data)<4: 
                return render_template('index.html'), 302
            return render_template('index.html', result=result, data = data)
        else:
        # Если метод запроса GET, отображаем шаблон без результата
            return render_template('index.html', data = data),print(angle)
        
            

    #except KeyError:
        
    
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
