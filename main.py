import os
import statistics
import tempfile
import uuid
from flask_cors import CORS

from flask import Flask, request, abort

app = Flask(__name__)
CORS(app)

@app.route("/hello")
def hello():
    return "Hello wolrd !"


# http://localhost:8080/hello
# { "username": "Benjamin" }
# curl --request POST --url http://localhost

@app.route("/hello", methods=['POST'])
def helloPost():
    json = request.get_json()
    return f"Hello {json['username']} !"


# http://localhost:8080/hello/Benjamin
# http://127.0.0.1:8080/hello/Benjamin


@app.route("/hello/<path:path>")
def toto(path):
    lang = request.args.get("lang")
    print(f"info : {request.args}")
    if lang == "fr":
        return f"Bonjour {path}"

    return f"Hello {path}"


@app.route("/helloPicture", methods=['POST'])
def helloPicture():
    file = extractFileFromPostRequest()
    return f"Merci pour l'image, nous l'avons stockée ici: {file}"


def extractFileFromPostRequest():
    if 'file' not in request.files or request.files['file'].filename == '':
        print("**** no file in POST Request")
        abort(500)
    file = request.files['file']
    tmpDir = tempfile.gettempdir()
    tmpName = str(uuid.uuid4())
    tmpFile = os.path.join(tmpDir, tmpName)
    file.save(tmpFile)
    return tmpFile


notes = {"Benjamin": [10, 12, 14], "François": [20, 18, 15], "Sylvain": [17, 16, 19]}


@app.route("/notes/<path:eleve>", methods=["POST"])
def post_notes(eleve):
    note = request.args.get("note")
    if eleve not in notes.keys():
        notes[eleve] = []
    notes[eleve].append(int(note))
    print(f"notes eleve: {notes}")
    return "{\"status\": \"ok\"}"


@app.route("/notes/<path:eleve>", methods=["GET"])
def get_notes(eleve):
    if eleve not in notes.keys():
        # abort(404)
        return "{\"status\": \"ko\", \"error\": \"Unknown eleve\"}"
    eleveNote = notes[eleve]
    return f"{{\"status\": \"ok\", \"data\": {eleveNote} }}"


@app.route("/moyenne/<path:eleve>", methods=["GET"])
def get_moyenne(eleve):
    if eleve not in notes.keys():
        # abort(404)
        return "{\"status\": \"ko\", \"error\": \"Unknown eleve\"}"
    moyenne = statistics.mean(notes[eleve])
    print(moyenne)
    return f"{{\"status\": \"ok\", \"data\": {str(moyenne)} }}"


@app.route("/eleves")
def get_eleves():
    return f"{{\"status\": \"ok\", \"data\": {list(notes.keys())} }}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
