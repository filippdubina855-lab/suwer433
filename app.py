from flask import Flask, request, jsonify
from models import db, HomeWork

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

API_KEY = "12345"


@app.route("/")
def home():
    return "Сервер работает!"


@app.route("/api/get_homework", methods=["POST"])
def get_homework():
    api_key = request.headers.get("X-API-Key")

    if not api_key:
        return jsonify({
            "error": "API-ключ отсутствует"
        }), 401

    if api_key != API_KEY:
        return jsonify({
            "error": "Неверный API-ключ"
        }), 401

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Пустое тело запроса"
        }), 400

    if "group" not in data:
        return jsonify({
            "error": "Группа не указана"
        }), 400

    group = data["group"]

    homework = HomeWork.query.filter_by(group=group).all()

    if not homework:
        return jsonify({
            "error": "Такой группы нет в базе данных"
        }), 404

    result = []

    for hw in homework:
        result.append({
            "id": hw.id,
            "title": hw.title,
            "body": hw.body,
            "group": hw.group,
            "header_url": hw.header_url
        })

    return jsonify(result), 200


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)