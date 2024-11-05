from flask import Flask, jsonify
from flask_cors import CORS
from flask import abort


app = Flask(__name__)
CORS(app)
data = {
    "cards": [
        {"id": 1, "title": "Карточка 1", "description": "Описание для карточки 1"},
        {"id": 2, "title": "Карточка 2", "description": "Описание для карточки 2"},
        {"id": 3, "title": "Карточка 3", "description": "Описание для карточки 3"}
    ]
}

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"cards": [{"id": x} for x in range(1, 4)]})


@app.route('/api/data/<int:data_id>')
def get_data_by_id(data_id):
    if data_id > len(data["cards"]) or data_id <= 0:
        abort(404)
    return jsonify(data["cards"][data_id - 1])


if __name__ == '__main__':
    app.run(debug=True)

