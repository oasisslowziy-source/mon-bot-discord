from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Bot Discord en ligne !"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()
    print("  ✔ Serveur keep_alive démarré sur le port 8080")
