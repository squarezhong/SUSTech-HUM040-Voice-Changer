# SUSTech-HUM040-Voice-Changer

[English](README.md) | [简体中文](README_cn.md)

## Introduction

Github: [squarezhong/SUSTech-HUM040-Voice-Changer](https://github.com/squarezhong/SUSTech-HUM040-Voice-Changer)

This is a project for SUSTech HUM040 (Chinese Information Processing). 

You can record your voice, then do emotion analysis and voice conversion.

![frontend](frontend.png)

### Emotion analysis
- Model: [xmj2002/hubert-base-ch-speech-emotion-recognition](https://huggingface.co/xmj2002/hubert-base-ch-speech-emotion-recognition)

### Voice conversion
ASR + VC
- ASR: [openai/whispering-small](https://huggingface.co/openai/whisper-small)
- VC: [huangxu1991/GPT-SoVITS-VC](https://github.com/huangxu1991/GPT-SoVITS-VC)

## Usage

Make sure the frontend and backend are running at the same time.

### Frontend

Make sure you have installed Node.js and npm.

```bash
cd frontend
npm install
npm run build
npm run dev
```

Visit the website shown in the console.

**Please allow the browser to access the microphone.**

### Backend

You can refer to  the "backend/example.py" file to wirte your own backend.

```bash
# install transformers
pip install transformers
# install speechbrain
pip install speechbrain
# if you don't have flask and flask-cors
pip install flask flask-cors
cd backend
# change it to the exact file name
python example.py
```

The implementation of voice conversion is really absurd, it is **not recommended** to use it.

If you really want to use it, please refer to the following steps.

1. Clone the [GPT-SoVITS-VC](https://github.com/huangxu1991/GPT-SoVITS-VC) repository in the backend directory.
2. Follow the instructions in the repository to install the dependencies and download the pre-trained model.
3. Add a blank `__init__.py` file in the `GPT-SoVITS-VC` directory.
4. Copy the `vc_nogui_bak.py` file to the `GPT-SoVITS-VC` directory and rename it to `vc_nogui.py`.
5. start the backend server.

You can substitute "sample.py" with your desired audio file (**between 3 and 10 seconds**).


## Development

Fork this repository, add your code, and submit a pull request.

### Emotion Analysis


### GPT-SoVITS Voice Conversion

The official version of [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) has not publish voice conversion feature yet. Therefore, we use a [fork](https://github.com/huangxu1991/GPT-SoVITS-VC) that has implemented that. 

You can help develop the above projects or just wait for their updates.

It is highly discouraged to reference the code in example.py for the voice conversion part, as its implementation is very unreasonable and is merely for demonstration purposes.

GPT-SoVITS-VC comes with its own WebUI, but since I want to use both sentiment analysis and voice conversion on my frontend page, I chose to implement it by calling Python functions.

Out of convenience, I didn't write it from scratch; instead, I modified vc_webui.py (essentially just removing the code related to the Gradio interface), which is equivalent to copying the function corresponding to the "Start Inference" button in the Gradio interface.

## References
1. [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)
2. [huangxu1991/GPT-SoVITS-VC](https://github.com/huangxu1991/GPT-SoVITS-VC)

## Contributors

This project exists thanks to all the people who contribute.

<a href="https://github.com/squarezhong/SUSTech-HUM040-Voice-Changer/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=squarezhong/SUSTech-HUM040-Voice-Changer" />
</a>

## License
[Apache License 2.0](LICENSE)
