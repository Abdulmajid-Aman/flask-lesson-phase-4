from app import app
from models import db, User, Profile

with app.app_context():
    print('Seeding information')

    User.query.delete()

    # Adding users to the database
    user1 = User(username='Abdulmajid', age=20)
    user2 = User(username='Abdullahi', age=22)
    user3 = User(username='Abdulqafar', age=22)
    user4 = User(username='Abdulrahman', age=22)
    user5 = User(username='Abdulaziz', age=22)

    db.session.add_all([user1, user2, user3, user4, user5])
    db.session.commit()  # Commit the changes to the User objects

    # Adding profiles to the database
    profile1 = Profile(bio="Lovely", user_id=user1.id)
    profile2 = Profile(bio="Good", user_id=user2.id)
    profile3 = Profile(bio="Nice", user_id=user3.id)
    profile4 = Profile(bio="Great", user_id=user4.id)
    profile5 = Profile(bio="Excellent", user_id=user5.id)

    db.session.add_all([profile1, profile2, profile3, profile4, profile5])
    db.session.commit()

    print('Done seeding')