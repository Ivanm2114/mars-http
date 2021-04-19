import os

from flask import Flask, request
import logging
import json
import random

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

# создаем словарь, в котором ключ — название города,
# а значение — массив, где перечислены id картинок,
# которые мы записали в прошлом пункте.

cities = {
    'москва': ['1540737/daa6e420d33102bf6947',
               '213044/7df73ae4cc715175059e'],
    'нью-йорк': ['1652229/728d5c86707054d4745f',
                 '1030494/aca7ed7acefde2606bdc'],
    'париж': ["1652229/f77136c2364eb90a3ea8",
              '3450494/aca7ed7acefde22341bdc']
}

# создаем словарь, где для каждого пользователя
# мы будем хранить его имя
sessionStorage = {}

city = ''


@app.route('/post', methods=['POST'])
def main():
    logging.info(f'Request: {request.json!r}')
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(response, request.json)
    logging.info(f'Response: {response!r}')
    return json.dumps(response)


def handle_dialog(res, req):
    global city
    user_id = req['session']['user_id']

    # если пользователь новый, то просим его представиться.
    if req['session']['new']:
        res['response']['text'] = 'Привет! Назови свое имя!'
        # создаем словарь в который в будущем положим имя пользователя
        sessionStorage[user_id] = {
            'first_name': None
        }
        return

    # если пользователь не новый, то попадаем сюда.
    # если поле имени пустое, то это говорит о том,
    # что пользователь еще не представился.
    if sessionStorage[user_id]['first_name'] is None:
        # в последнем его сообщение ищем имя.
        first_name = get_first_name(req)
        # если не нашли, то сообщаем пользователю что не расслышали.
        if first_name is None:
            res['response']['text'] = \
                'Не расслышала имя. Повтори, пожалуйста!'
        # если нашли, то приветствуем пользователя.
        # И спрашиваем какой город он хочет увидеть.
        else:
            sessionStorage[user_id]['first_name'] = first_name
            res['response'][
                'text'] = 'Приятно познакомиться, ' \
                          + first_name.title() \
                          + '. Я - Алиса. Угадаешь город?'
            res['response']['buttons'] = [
                {
                    'title': el,
                    'hide': True
                } for el in ['Да', 'Нет', 'Помощь']
            ]

    elif req['request']["original_utterance"] == 'Да':
        res['response']['text'] = 'Хорошо'
        city = random.choice(list(cities.keys()))
        if city in cities:
            res['response']['card'] = {}
            res['response']['card']['type'] = 'BigImage'
            res['response']['card']['image_id'] = random.choice(cities[city])
            res['response']['card']['title'] = 'Какой город?'
            res['response']['buttons'] = [
                {
                    'title': el,
                    'hide': True
                } for el in ['Помощь']
            ]
    elif req['request']["original_utterance"] == 'Нет':
        res['response']['text'] = 'Ну и ладно'
        res['response']['end_session'] = True
        return
    elif req['request']['original_utterance'] == 'Помощь':
        res['response']['text'] = 'Я показываю вам город, а вы должны его угадать\n Сыграем'
        res['response']['buttons'] = [
            {
                'title': el,
                'hide': True
            } for el in ['Да', 'Нет', 'Помощь']
        ]
    else:
        if req['request']['nlu']['entities'][0]['value']['city'] == city:
            res['response']['text'] = 'Правильно'
            res['response']['end_session'] = True
            return
        else:
            res['response']['text'] = \
                'Неправильно. Попробуй еще разок!'
            res['response']['buttons'] = [
                {
                    'title': el,
                    'hide': True
                } for el in ['Помощь']
            ]


def get_city(req):
    # перебираем именованные сущности
    for entity in req['request']['nlu']['entities']:
        # если тип YANDEX.GEO то пытаемся получить город(city),
        # если нет, то возвращаем None
        if entity['type'] == 'YANDEX.GEO':
            # возвращаем None, если не нашли сущности с типом YANDEX.GEO
            return entity['value'].get('city', None)


def get_first_name(req):
    # перебираем сущности
    for entity in req['request']['nlu']['entities']:
        # находим сущность с типом 'YANDEX.FIO'
        if entity['type'] == 'YANDEX.FIO':
            # Если есть сущность с ключом 'first_name',
            # то возвращаем ее значение.
            # Во всех остальных случаях возвращаем None.
            return entity['value'].get('first_name', None)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
