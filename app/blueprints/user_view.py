from flask import Blueprint, jsonify, request, flash
from app.models import User, db
from app.form import LoginForm, RegisterForm


user_bp = Blueprint("user", __name__)

@user_bp.route("/user", methods=["POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        exist_user = User.get_user_by_email(email)
        if exist_user:
            return jsonify('사용 중인 이메일 입니다.'), 400
        
        new_user = User(name=name, email=email)
        new_user.set_password(password)
    
        db.session.add(new_user)
        db.session.commit()
    return jsonify({"id": new_user.id, "name": new_user.name, "email": new_user.email})


@user_bp.route("/user", methods=['GET'])
def get_user_by_id():
    users = User.get_all_users()
    return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])


@user_bp.route('/user', methods=['DELETE'])
def delete_user():
    name = request.get_json()['name']
    User.delete(name)
    return jsonify({'message': 'User deleted'})