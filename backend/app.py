import os
from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GENAI_API_KEY = os.getenv("GENAI_API_KEY")
if GENAI_API_KEY:
    genai.configure(api_key=GENAI_API_KEY)
else:
    raise ValueError("Missing Google Gemini API Key!")

@app.route('/process', methods=['POST'])
def process_code():
    data = request.get_json(silent=True)
    
    if not data or "code" not in data or "prompt" not in data:
        return jsonify({"error": "Invalid or missing JSON data"}), 400
    
    user_code = data["code"]
    user_prompt = data["prompt"]
    
    model = genai.GenerativeModel('gemini-pro')
    
    response = model.generate_content(f"{user_prompt}:\n\n{user_code}")
    
    return jsonify({"response": response.text if response else "No response"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
