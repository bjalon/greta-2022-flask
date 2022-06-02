from flask import Flask

app = Flask(__name__)

@app.route("/tweets/1")
def tweet1():
    return "{\"author\": \"Benjamin JALON\", \"content\":\"Bonjour tout le monde\"}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)