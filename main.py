from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["SECRET_KEY"] = 'sinergy'

notes = [
    {"id": 0, "topic": "rest api"},
    {"id": 1, "uni": "sinergy"},
    {"id": 2, "lis": "rodogor"}
]

# GET все заметки - ДОБАВЛЕНО
@app.route('/api/notes', methods=['GET'])
def get_all_notes():
    return jsonify(notes)

# GET конкретная заметка
@app.route('/api/get/<int:notes_index>', methods=['GET'])
def get_tasks(notes_index):
    return jsonify(notes[notes_index])

# POST добавить заметку
@app.route('/api/task', methods=['POST'])
def add_note():
    data = request.get_json()
    new_note = data
    new_note["id"] = len(notes)
    notes.append(new_note)
    return jsonify({'note': new_note}), 201

# DELETE удалить заметку
@app.route('/api/delete/<int:to_delete>', methods=['DELETE'])
def delete_note(to_delete):
    del notes[to_delete]
    return jsonify(notes)

# PUT изменить заметку - ИСПРАВЛЕНО
@app.route('/api/put/<int:to_edit>', methods=['PUT'])
def edit_note(to_edit):
    data = request.get_json()
    notes[to_edit].update(data)
    return jsonify(notes[to_edit])

if __name__ == "__main__":
    app.run(debug=True, port=5000)