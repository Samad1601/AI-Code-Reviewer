from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

genai.configure(api_key="AIzaSyA4ROZHE0Yz3NQ_UF58atzaHByv3AWyxrU")

@app.route('/process', methods=['POST'])
def process_code():
    data = request.json
    user_code = data.get("code")
    user_prompt = data.get("prompt")

    if not user_code or not user_prompt:
        return jsonify({"error": "Code and prompt are required"}), 400

    response = genai.generate_content(f"{user_prompt}:\n\n{user_code}")
    
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(debug=True)
