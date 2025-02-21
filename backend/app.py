from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

genai.configure(api_key="AIzaSyBxk5p1hvfbmK5TqsOssOqte_cDRHLTIbw")

@app.route('/process', methods=['POST'])
def process_code():
    data = request.get_json(silent=True)
    
    if not data or "code" not in data or "prompt" not in data:
        return jsonify({"error": "Invalid or missing JSON data"}), 400

    user_code = data["code"]
    user_prompt = data["prompt"]

    # Initialize the model
    model = genai.GenerativeModel('gemini-pro')

    # Generate content
    response = model.generate_content(f"{user_prompt}:\n\n{user_code}")

    return jsonify({"response": response.text if response else "No response"})

if __name__ == '__main__':
    app.run(debug=True)