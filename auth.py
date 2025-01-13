from flask import jsonify, request, Blueprint, flash , session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from database import session as db_session , User
from flask_bcrypt import Bcrypt

auth_bp = Blueprint("auth",__name__)
bcrypt = Bcrypt()

#register route
@auth_bp.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        try:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')
            role = data.get('role')

            if not email or not password or not role:
                return jsonify({"message":"Email , Password , and role are required"}), 400

            #Encrypting the password
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(email=email,password= hashed_password,role=role)
            db_session.add(new_user)
            db_session.commit()

            #cookies
            session['user_id'] = new_user.id
            flash('Registered successfully!','success')
            return jsonify({"message":"Registered successful","success":True}),200

        except IntegrityError:
            db_session.rollback()
            return jsonify({"message":"Email already exists"}),400
        except SQLAlchemyError as e:
            db_session.rollback()
            return jsonify({"message":"Database error","error":str(e)}), 500
        except Exception as e:
            return jsonify({"message":"An error occurred","error":str(e)})
    return jsonify({"message":"Bad request"}),400

#Login route
@auth_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        try:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')
            user = db_session.query(User).filter_by(email=email).first()

            if user and bcrypt.check_password_hash(user.password,password):
                session['user_id'] = user.id
                flash('Logged in successfully!', 'success')
                return jsonify({"message":"Login successful"}), 200
            else:
                flash('Invalid credentials', 'danger')
                return jsonify({"message":"Invalid credentials"}),400
        except SQLAlchemyError as e:
            db_session.rollback()
            return jsonify({"message":"Database error","error": str(e)}), 500
        except Exception as e:
            return jsonify({"message":"An error occurred", "error": str(e)}), 500

    return jsonify({"message":"Bad request"}), 400

@auth_bp.route('/logout', methods=['POST'])
def logout():
    try:
        session.pop('user_id',None)
        flash('Logged out successfully!', 'success')
        return jsonify({"message":"Logout successful"}),200
    except Exception as e:
        return jsonify({"message":"An error occurred","error":str(e)}),500


#This route is to check if user is already authenticated
@auth_bp.route('/status', methods=['GET'])
def auth_status():
    if 'user_id' in session:
        return jsonify({"authenticated":True , "user_id":session["user_id"]})
    else:
        return jsonify({"authenticated": False}), 200

