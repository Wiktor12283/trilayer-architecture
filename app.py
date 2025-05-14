from flask import Flask, request, jsonify
from repository.user_repository import UserRepository
from service.user_service import UserService
from datetime import datetime

def create_app():
    app = Flask(__name__)
    repo = UserRepository()
    service = UserService(repo)

    @app.route("/users", methods=["GET"])
    def get_users():
        now = datetime.now().year
        users = [u.to_dict(now) for u in service.get_all_users()]
        return jsonify(users), 200

    @app.route("/users/<int:user_id>", methods=["GET"])
    def get_user(user_id):
        user = service.get_user(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user.to_dict(datetime.now().year)), 200

    @app.route("/users", methods=["POST"])
    def create_user():
        data = request.json
        try:
            user = service.create_user(data)
            return jsonify(user.to_dict(datetime.now().year)), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/users/<int:user_id>", methods=["PATCH"])
    def update_user(user_id):
        data = request.json
        try:
            user = service.update_user(user_id, data)
            if not user:
                return jsonify({"error": "User not found"}), 404
            return jsonify(user.to_dict(datetime.now().year)), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    @app.route("/users/<int:user_id>", methods=["DELETE"])
    def delete_user(user_id):
        user = service.delete_user(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        return '', 204

    return app

if __name__ == "__main__":
    create_app().run(debug=True)
