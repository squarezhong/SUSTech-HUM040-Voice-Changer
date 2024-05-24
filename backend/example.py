from flask import Flask, request, send_file, jsonify
from flask_cors import CORS

import io
import os

import librosa
import soundfile
import numpy as np
import pickle
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
def extract_feature(file_name,mfcc,chroma,mel):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        result = np.array([])
        sample_rate = sound_file.samplerate
        if  mfcc:
            mfccs = np.mean(librosa.feature.mfcc(y=X,sr=sample_rate,n_mfcc=40).T,axis=0)
            result = np.hstack((result,mfccs))
        if chroma:
            stft = np.abs(librosa.stft(X))
            chroma = np.mean(librosa.feature.chroma_stft(S=stft,sr=sample_rate).T,axis=0)
            result = np.hstack((result,chroma))
        if mel:
            mel = np.mean(librosa.feature.melspectrogram(y=X,sr=sample_rate).T,axis=0)
            result = np.hstack((result,mel))
        return result
emotions ={
    "01":"neutral",
    "02":"calm",
    "03":"happy",
    "04":"sad",
    "05":"angry",
    "06":"fearful",
    "07":"disgust",
    "08":"surprised",
}
# Load the pre-trained model
with open('emotion_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def perform_emotion_analysis(file, sample_rate):
    # Extract features from the audio file
    feature = extract_feature(file, mfcc=True, chroma=True, mel=True)
    feature = feature.reshape(1, -1)
    # Predict the emotion using the pre-trained model
    predicted_emotion = model.predict(feature)[0]
    #print(predicted_emotion)
    #predicted_emotion = emotions[predicted_emotion_code]
    # Obtain the confidence level of the prediction
    #confidence = max(model.predict_proba(feature)[0])
    result = {"emotion": predicted_emotion}
    return result

def perform_voice_conversion(file, sample_rate):
    # TODO: implement voice conversion logic here
    converted_audio = file.read() 
    return converted_audio

if __name__ == '__main__':
    file = "02.wav"
    #file=os.path.basename(file)
    sample_rate = 22050  # Set the sample rate if necessary
    result = perform_emotion_analysis(file, sample_rate)
    #print(result)
    app.run(debug=True, host='0.0.0.0', port=14400)
