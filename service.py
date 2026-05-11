from flask import Flask, Response, request, jsonify
from constants import CONTEXT, MODEL, MODEL_MINI, MODEL_NANO, MODEL_FULL
from CVutils import read_text_file, filter_data, fill_template, html_to_pdf
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/filter", methods=["POST"])
def filter():

    payload = request.get_json()

    api_key = payload.get("api_key", "")
    model = payload.get("model", "")
    lang = payload.get("lang", "")
    position = payload.get("position", "")
    data = payload.get("data", {})
    
    models = {"nano": MODEL_NANO, "mini":MODEL_MINI, "full": MODEL_FULL}
    model  = models[model]

    filtered_data = filter_data(api_key, model, position, lang, data, CONTEXT)
    
    return jsonify(filtered_data)
    
@app.route("/html", methods=["POST"])
def html():
    payload = request.get_json()

    data = payload.get("data", {})

    template = read_text_file('files/atsSafeTemplate.html')                

    html = fill_template(data, template)
    
    return Response(html)

@app.route("/pdf", methods=["POST"])
def pdf():
    payload = request.get_json()

    html = payload.get("data", "")
    
    file = html_to_pdf(html)
    
    return Response(file)

@app.route("/health")
def health():
    return {"status": "OK"}, 200

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
