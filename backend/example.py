from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import io
import os
import sys
import emotion_analysis

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['sample']
    sample_rate = request.form['sampleRate']

    # process audio file (emotion analysis or voice conversion)
    if request.args.get('type') == 'analysis':
        print("emotion analysis")
        result = perform_emotion_analysis(file, sample_rate)
        print(result)
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
    predicted_emotion = emotion_analysis.predict_emotion(file)
    result = {"emotion": predicted_emotion}
    return result

def perform_voice_conversion(file, sample_rate):
    """very abstract implementation of voice conversion

    Args:
        file (_type_): audio file in binary format
        sample_rate (_type_): sample rate of the audio file

    Returns:
        _type_: audio file in binary format
    """
    
    # start the show
    original_working_directory = os.getcwd()
    
    # change to the directory of GPT-SoVITS-VC
    os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), 'GPT-SoVITS-VC')))
    sys.path.append(os.getcwd())
    
    from scipy.io import wavfile
    from voice_conversion import vc_main
    from tools.i18n.i18n import I18nAuto
    i18n = I18nAuto()
    
    # store the audio file first
    with open("input.wav", "wb") as f:
        f.write(file.read())

    # perform voice conversion
    # TODO: STT
    sampling_rate, audio_int16 = next(vc_main("input.wav", "今天的天气非常好", i18n("中文"), "../sample.wav"))
    
    # you can also save the converted audio file
    wavfile.write("../output.wav", sampling_rate, audio_int16)
    
    os.chdir(original_working_directory)

    # return the converted audio file
    with open("output.wav", "rb") as f:
        return f.read()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=14400)


    