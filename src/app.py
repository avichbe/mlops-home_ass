from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
import BL.model_bl
import model.model_load as loader

# Initialize the Flask app
app = Flask(__name__)

pipeline = loader.ModelLoad.load_model()

# Define a route to handle NER requests
@app.route('/ner', methods=['POST'])
def ner():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    else:
        result = BL.model_bl.simple_prediction(pipeline,text)
    
    return jsonify(result)

# Define a health check route
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)