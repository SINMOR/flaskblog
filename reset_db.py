from flaskblog import db, app

with app.app_context():
    db.drop_all()
    db.create_all()
    print("Database has been reset.")