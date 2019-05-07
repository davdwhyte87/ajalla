from flask import Blueprint, jsonify


user=Blueprint('user',__name__,template_folder='templates')

@user.route('/')
def register():
    return jsonify(message="Holla how are you")