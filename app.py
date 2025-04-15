from flask import Flask, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)

# Set your API key (preferably from environment variable for security)
genai.configure(api_key="AIzaSyCsb53oK-NQJd7OprTpFnLHGEDU1JESVOQ")  # WARNING: Don't hardcode in production!

@app.route('/api/generate', methods=['POST'])
def generate_text():
    try:
        data = request.get_json()
        prompt = data.get('prompt')

        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400

        # Create generative model
        model = genai.GenerativeModel('gemini-pro')
        
        # Use generate_content instead of chat if just using one prompt
        response = model.generate_content(prompt.strip())

        return jsonify({'result': response.text}), 200

    except Exception as e:
        print(f"[ERROR] {e}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use PORT env if set (for Render, Heroku, etc.)
    app.run(host='0.0.0.0', port=port)
