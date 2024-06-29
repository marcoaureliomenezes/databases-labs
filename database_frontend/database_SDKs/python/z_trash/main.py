from flask_sqlalchemy import db, User

print(User.query.all())