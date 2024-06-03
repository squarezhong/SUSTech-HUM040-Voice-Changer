import librosa
import os
import sys
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from scipy.io import wavfile

# load model and processor
processor = WhisperProcessor.from_pretrained("openai/whisper-small")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")
model.config.forced_decoder_ids = None

def whisper_asr(file_path):
    # load local audio file
    audio, sampling_rate = librosa.load(file_path, sr=None)
    
    # resample the audio to 16000 Hz if it's not already at 16000 Hz
    target_sampling_rate = 16000
    if sampling_rate != target_sampling_rate:
        audio = librosa.resample(audio, orig_sr=sampling_rate, target_sr=target_sampling_rate)

    # process the audio file
    input_features = processor(audio, sampling_rate=target_sampling_rate, return_tensors="pt").input_features 

    # generate token ids
    predicted_ids = model.generate(input_features)

    # decode token ids to text
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
    
    return transcription[0]

def sovits_conversion(file_path):
    """very abstract implementation of voice conversion

    Args:
        file (_type_): audio file in binary format
        sample_rate (_type_): sample rate of the audio file

    Returns:
        _type_: audio file in binary format
    """
    
    # asr 
    text = whisper_asr(file_path)
    
    # start the show
    original_working_directory = os.getcwd()
    
    # change to the directory of GPT-SoVITS-VC
    os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), 'GPT-SoVITS-VC')))
    sys.path.append(os.getcwd())
    
    from vc_nogui import vc_main
    from tools.i18n.i18n import I18nAuto

    i18n = I18nAuto()
    
    # perform voice conversion
    sampling_rate, audio_int16 = next(vc_main("../input.wav", text, i18n("中文"), "../sample.wav"))
    
    # you can also save the converted audio file
    wavfile.write("../output.wav", sampling_rate, audio_int16)
    
    os.chdir(original_working_directory)

    # return the converted audio file
    with open("output.wav", "rb") as f:
        return f.read()

if __name__ == '__main__':
    # test the asr function
    audio_path = "input.wav"  # replace with your audio file path

    transcription = whisper_asr(audio_path)

    # print the transcription
    print(transcription)
    
    # sovits_conversion(audio_path)