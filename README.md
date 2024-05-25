# SUSTech-HUM040-Voice-Changer

## Introduction

This is a project for SUSTech HUM040 (Chinese Information Processing). 

You can record your voice, then do emotion analysis and voice conversion.

## Usage

### Frontend

Make sure you have installed Node.js and npm.

```bash
cd frontend
npm install
npm run build
npm run dev
```

Visit the website shown in the console.

**请允许浏览器访问麦克风。**

**Please allow the browser to access the microphone.**

### Backend
```bash
# if you don't have flask and flask-cors
pip install flask flask-cors
cd backend
# change it to the exact file name
python example.py
```

## Development

Fork this repository, add your code, and submit a pull request.

### Emotion Analysis

[Datasets](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio/data)

To keep the project neat, extracted dataset is not included in this repository. You can download it from the link above.

### GPT-SoVITS Voice Conversion

## Contributors

This project exists thanks to all the people who contribute.

<a href="https://github.com/squarezhong/SUSTech-HUM040-Voice-Changer/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=squarezhong/SUSTech-HUM040-Voice-Changer" />
</a>

## License
Apache License 2.0
