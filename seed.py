from app import app
from models import db, User

with app.app_context():
    print('Seeding information')

    db.session.add(User(username='Abdulmajid', age = 20))
    db.session.add(User(username='Abdullahi', age = 22))
    db.session.add(User(username='Abdulqafar', age = 22))
    db.session.add(User(username='Abdulrahman', age = 22))
    db.session.add(User(username='Abdulaziz', age = 22))


    db.session.commit()

    print('Done seeding')