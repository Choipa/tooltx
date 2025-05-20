from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Cho phép tất cả các nguồn truy cập API

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    seq = data.get('sequence', '').upper()
    seq = ''.join(c for c in seq if c in ['T', 'X'])

    count_t = seq.count('T')
    count_x = seq.count('X')
    total = count_t + count_x

    if total == 0:
        return jsonify(prediction='N', confidence=0.5)

    prob_t = count_t / total
    prob_x = count_x / total

    if prob_t > prob_x:
        return jsonify(prediction='T', confidence=round(prob_t, 2))
    elif prob_x > prob_t:
        return jsonify(prediction='X', confidence=round(prob_x, 2))
    else:
        return jsonify(prediction='N', confidence=0.5)
