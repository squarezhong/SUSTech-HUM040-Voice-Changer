from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['sample']
    sample_rate = request.form['sampleRate']

    # process audio file (emotion analysis or voice conversion)
    if request.args.get('type') == 'analysis':
        result = perform_emotion_analysis(file, sample_rate)
        return jsonify(result)
    else:
        print("voice conversion")
        result_audio = perform_voice_conversion(file, sample_rate)
        return send_file(
            io.BytesIO(result_audio),
            mimetype='audio/wav',
            as_attachment=False
        )

def perform_emotion_analysis(file, sample_rate):
    # TODO: implement emotion analysis logic here
    result = {"emotion": "happy", "confidence": 0.98}
    return result

def perform_voice_conversion(file, sample_rate):
    # TODO: implement voice conversion logic here
    converted_audio = file.read() 
    return converted_audio

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=14400)
