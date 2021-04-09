from requests import post, delete, put, get

print(get('http://localhost:5000/api/v2/users').json())

print(get('http://localhost:5000/api/v2/users/1').json())

print(post('http://localhost:5000/api/v2/users',
           json={'id': 4,
                 'surname': 'Puchkov',
                 'name': 'Kirill',
                 'age': 14,
                 'position': 'Sergant',
                 'speciality': 'Front End Developer',
                 'address': 'module 2',
                 'email': 'sromniykika@mail.ru',
                 'hometown': 'Saint-Petersburg'
                 }).json())

print(get('http://localhost:5000/api/v2/users/4').json())

print(put('http://localhost:5000/api/v2/users/4', json={'surname': 'Puhkov',
                                                        'name': 'Kiril',
                                                        'age': 13,
                                                        'position': 'Sergant',
                                                        'speciality': 'Front End Developer',
                                                        'address': 'module 3',
                                                        'email': 'sromniy@mail.ru',
                                                        'hometown': 'Saint-Petersburg'
                                                        }).json())

print(get('http://localhost:5000/api/users/4').json())

print(delete('http://localhost:5000/api/users/4').json())

print(get('http://localhost:5000/api/users/4').json())
