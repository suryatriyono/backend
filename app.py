from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')

    # Kirim pertanyaan ke Rasa
    rasa_response = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"sender": "user", "message": question})
    rasa_response = rasa_response.json()

    if rasa_response:
        answer = rasa_response[0]['text']
    else:
        answer = "Maaf, saya tidak mengerti pertanyaan Anda. Bisa coba tanyakan dengan cara lain?"

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
