from flask import Flask, jsonify, send_from_directory
import random
import os

app = Flask(__name__)

@app.route("/")
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route("/cards")
def get_cards():
    suits = ['Hjärter', 'Ruter', 'Spader', 'Klöver']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Kn', 'D', 'K', 'E']
    deck = [f"{r} {s}" for s in suits for r in ranks]
    random.shuffle(deck)
    return jsonify(deck[:5])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
