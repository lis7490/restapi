from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["SECRET_KEY"] = 'sinergy'

# Начальные данные
notes = [
    {"id": 0, "topic": "rest api"},
    {"id": 1, "uni": "sinergy"},
    {"id": 2, "lis": "rodogor"}
]


# GET - получить все заметки
@app.route('/api/notes', methods=['GET'])
def get_all_notes():
    return jsonify(notes)


# GET - получить конкретную заметку
@app.route('/api/notes/<int:notes_index>', methods=['GET'])
def get_note(notes_index):
    if notes_index < 0 or notes_index >= len(notes):
        return jsonify({"error": "Note not found"}), 404
    return jsonify(notes[notes_index])


# POST - добавить новую заметку
@app.route('/api/notes/post', methods=['POST'])
def add_note():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Добавляем ID к новой заметке
        new_note = data
        new_note["id"] = len(notes)
        notes.append(new_note)

        return jsonify({"note": new_note, "message": "Note added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# DELETE - удалить заметку
@app.route('/api/notes/delete/<int:to_delete>')
def delete_note(to_delete):
    del notes[to_delete]
    return notes


# PUT - изменить заметку
@app.route('/api/notes/<int:to_edit>', methods=['PUT'])
def edit_note(to_edit):
    if to_edit < 0 or to_edit >= len(notes):
        return jsonify({"error": "Note not found"}), 404

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Обновляем заметку
        notes[to_edit].update(data)

        return jsonify({"updated_note": notes[to_edit]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)