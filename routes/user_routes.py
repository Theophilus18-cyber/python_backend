from flask import Blueprint
from controllers.user_controller import index,users,fetch_user_id,delete_user_by_id

user_bp = Blueprint('user_bp',__name__)

user_bp.route('/',methods=['GET','POST'])(index)
user_bp.route('/users',methods=['GET'])(users)
user_bp.route('/users/<int:user_id>', methods=['GET'])(fetch_user_id)
user_bp.route('/users/<int:user_id>', methods=['DELETE'])(delete_user_by_id)