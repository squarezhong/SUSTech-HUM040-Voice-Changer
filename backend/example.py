from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import io
import os
import sys
from emotion_analysis_hubert import predict_emotion
from voice_conversion import sovits_conversion

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['sample']
    sample_rate = request.form['sampleRate']
    
    # store the audio file first
    with open("input.wav", "wb") as f:
        f.write(file.read())

    # process audio file (emotion analysis or voice conversion)
    if request.args.get('type') == 'analysis':
        print("emotion analysis")
        result = perform_emotion_analysis("input.wav", sample_rate)
        print(result)
        return jsonify(result)
    else:
        print("voice conversion")
        result_audio = perform_voice_conversion("input.wav", sample_rate)
        return send_file(
            io.BytesIO(result_audio),
            mimetype='audio/wav',
            as_attachment=False
        )

def perform_emotion_analysis(file_path, sample_rate):
    return predict_emotion(file_path)

def perform_voice_conversion(file_path, sample_rate):
    return sovits_conversion(file_path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=14400)


    