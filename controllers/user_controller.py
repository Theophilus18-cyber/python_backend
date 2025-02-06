from flask import render_template, request, redirect, jsonify
from models.users import insert_user, fetch_all_users, get_by_id, delete_user

def index():
    if request.method == 'POST':
        user_details = request.form
        name = user_details.get('name')
        email = user_details.get('email')
        if not name or not email:
            return "Name and email are required", 400
        insert_user(name, email)
        return redirect('/users')
    return render_template('index.html')

def fetch_user_id(user_id):
    user_details = get_by_id(user_id)
    if user_details:
        return jsonify(user_details)
    else:
        return "User not found", 404

def users():
    user_details = fetch_all_users()
    return render_template('users.html', userDetails=user_details)

def delete_user_by_id(user_id):
    if delete_user(user_id):
        return jsonify({"message":"user delete succesfully"}),200
    else:
        return jsonify({"message":"user not found"}) , 404