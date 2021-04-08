from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()

    user1 = User()
    user1.surname = 'Scott'
    user1.name = 'Ridley'
    user1.age = 21
    user1.position = 'captain'
    user1.speciality = 'research engeneer'
    user1.address = 'module 1'
    user1.email = "scott_chief@mars.org"
    user1.hometown = 'New York'

    user2 = User()
    user2.surname = 'Elatskov'
    user2.name = 'Dimon'
    user2.age = 17
    user2.position = 'prgrammer'
    user2.speciality = 'engeneer'
    user2.address = 'module 69'
    user2.email = "dmela69@mars.org"
    user2.hometown = 'Moscow'

    user3 = User()
    user3.surname = 'Bon Jovi'
    user3.name = 'Jhon'
    user3.age = 77
    user3.position = 'musican'
    user3.speciality = 'entertainer'
    user3.address = 'module 4'
    user3.email = "musiconmars@mars.org"
    user3.hometown = 'Los Angeles'

    db_sess.add(user1)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.commit()


if __name__ == '__main__':
    main()
