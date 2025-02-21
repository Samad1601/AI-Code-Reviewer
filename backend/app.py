from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

genai.configure(api_key="AIzaSyA4ROZHE0Yz3NQ_UF58atzaHByv3AWyxrU")
@app.route('/process', methods=['POST'])
def process_code():
    data = request.get_data(as_text=True)
    print("Received raw data:", data)  # Debugging line

    try:
        json_data = request.get_json()
        print("Decoded JSON:", json_data)  # Debugging line

        user_code = json_data.get("code")
        user_prompt = json_data.get("prompt")

        if not user_code or not user_prompt:
            return jsonify({"error": "Code and prompt are required"}), 400

        response = genai.generate_content(f"{user_prompt}:\n\n{user_code}")
        return jsonify({"response": response.text})

    except Exception as e:
        print("JSON Decode Error:", str(e))
        return jsonify({"error": "Invalid JSON format"}), 400
