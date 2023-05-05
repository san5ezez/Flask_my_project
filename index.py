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
    #try:
        if request.method == 'POST':
            result = ''
            if len(data)<4: 
                return render_template('index.html'), 302
            return render_template('index.html', result=result, data = data)
        else:
        # Если метод запроса GET, отображаем шаблон без результата
            return render_template('index.html', data = data)
        
            

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


@app.route('/shot_game', methods=['POST'])
def game():
    first_angle = (50, 80)
    second_angle = (100, 130)
    third_angle = (150, 180)
    forth_angle = (200, 230)
    fifth_angle = (250, 280)


    all_cards_angles = [72, 144, 216, 288, 360]
    all_angles = [first_angle, second_angle, third_angle, forth_angle, fifth_angle]

    angle = request.form['angle']
    angle = int(angle)
    print("угол на старте", angle)
    for item in data:
        for angle_item in all_angles:
            print(angle_item)
            if angle in range(angle_item[0], angle_item[1]):
                print(angle)
                lay_angle = min(all_cards_angles, key=lambda x: abs(x - angle))
                print(lay_angle)
                try:
                    data.pop(all_cards_angles.index(lay_angle))
                except:
                    pass
                return render_template('index.html', data=data), 200
    return render_template('index.html', data=data), 200

if __name__ == '__main__':
    app.run (debug=True)
