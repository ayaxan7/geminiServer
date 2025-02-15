from flask import Flask, request, jsonify
import os
import google.generativeai as generativeai

app = Flask(__name__)

# Configure API key
generativeai.configure(api_key="AIzaSyCsb53oK-NQJd7OprTpFnLHGEDU1JESVOQ")

@app.route('/api/generate', methods=['POST'])
def generate_text():
    try:
        model = generativeai.GenerativeModel('gemini-pro')
        data = request.get_json()
        chat = model.start_chat()
        prompt = data.get('prompt')

        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400

        response = chat.send_message(prompt.strip())

        return jsonify({'result': response.text}), 200 if response.text else 500

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render provides a dynamic port
    app.run(host='0.0.0.0', port=port, debug=False)
