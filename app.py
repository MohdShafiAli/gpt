from flask import Flask, request, render_template, jsonify
import json
from prompt_processing import tokenizer
from knowledge_classification import classify,search
from knowledge_classification import extract,tokenizer as tk

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search",methods=["POST"])
def ser():
    data = request.get_json()
    prompt = data["prompt"]
    result = search(prompt)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)