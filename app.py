from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from model import llama_model

app = Flask(__name__)
CORS(app)


class APIAgent:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_pet_by_id(self, pet_id):
        response = requests.get(f"{self.base_url}/pet/{pet_id}")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.status_code}


agent = APIAgent("https://petstore.swagger.io/v2")
model_name = "facebook/llama-tiny"


@app.route("/generate", methods=["POST"])
def generate():
    model, tokenizer = llama_model(model_name)
    data = request.json

    # Check if 'text' is in the request data
    if "text" not in data:
        return jsonify({"error": 'Missing "text" field in the request'}), 400

    input_text = data["text"]

    # Tokenize input text
    inputs = tokenizer(input_text, return_tensors="pt")

    # Generate output
    outputs = model.generate(**inputs)

    # Check if outputs are generated
    if outputs is not None and len(outputs) > 0:
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    else:
        response = "No output generated."

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
