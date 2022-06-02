import os
import tempfile
import uuid

from flask import Flask, request, abort

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello wolrd !"


@app.route("/hello", methods=['POST'])
def helloPost():
    json = request.get_json()
    return f"Hello {json['username']} !"


# http://localhost:8080/hello/Benjamin
# http://127.0.0.1:8080/hello/Benjamin

@app.route("/hello/<path:path>")
def toto(path):
    lang = request.args.get("lang")
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
