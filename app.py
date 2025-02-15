from flask import Flask, request, jsonify
import os
import google.generativeai as generativeai

app = Flask(__name__)

# Configuration (API key should be set in environment variables)
generativeai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Removed hardcoded key

@app.route('/api/generate', methods=['POST'])
def generate_tex():
    try:
        # Initialize the text generation model
        model = generativeai.GenerativeModel('gemini-pro')
        data = request.get_json()
        chat = model.start_chat()
        prompt = data.get('prompt')

        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400

        
         # Correct model for text generation
        response = chat.send_message(prompt.rstrip().lstrip())

        if response.text:
            return jsonify({'result': response.text}), 200
        else:
            return jsonify({'error': 'No response from model'}), 500

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)