from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"
    
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