from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(5), nullable=False, default='user')  # 유저/관리자로 구분
    name = db.Column(db.String(80), nullable=False)  # 한국어로 20글자 정도
    email = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    

    def __repr__(self):
        return f"<User {self.name}>"
    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def create(cls, name: str, email: str) -> 'User':
        new_user = cls(name, email)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @classmethod
    def get_all_users(cls):
        return cls.query.all()
    
    @classmethod
    def get_user_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()


    @classmethod
    def read(cls, id: int=None, name: str=None) -> 'User':
        if id is not None:
            return cls.query.get(id)
        elif name is not None:
            user = cls.query.filter_by(name=name).first()
            return user
        return None
    
    
    @classmethod
    def delete(cls, name: str) -> None:
        user = cls.read(name=name)
        if user:
            db.session.delete(user)
            db.session.commit()
            return user
        return None