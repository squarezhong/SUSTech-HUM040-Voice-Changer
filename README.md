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

If you do not use the voice conversion feature, the following steps are enough.

```bash
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
4. Copy the `voice_conversion_bak.py` file to the `GPT-SoVITS-VC` directory and rename it to `voice_conversion.py`.
5. start the backend server:

You can substitute "sample.py" with your desired audio file (between 3 and 10 seconds).


## Development

Fork this repository, add your code, and submit a pull request.

### Emotion Analysis

You can train your own model with [ravdess-emotional-speech-audio/data](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio/data)

To keep the project neat, extracted dataset is not included in this repository. You can download it from the link above.

### GPT-SoVITS Voice Conversion

The official version of [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) has not publish voice conversion feature yet. Therefore, we use a [fork](https://github.com/huangxu1991/GPT-SoVITS-VC) that has implemented that. 

You can help develop the above projects or just wait for their updates.

It is highly discouraged to reference the code in example.py for the voice conversion part, as its implementation is very unreasonable and is merely for demonstration purposes.

GPT-SoVITS-VC comes with its own WebUI, but since I want to use both sentiment analysis and voice conversion on my frontend page, I chose to implement it by calling Python functions.

Out of convenience, I didn't write it from scratch; instead, I modified vc_webui.py (essentially just removing the code related to the Gradio interface), which is equivalent to copying the function corresponding to the "Start Inference" button in the Gradio interface.

非常不建议参考我在 example.py 中声音转换部分的代码，其实现非常不合理，仅仅是为了演示。

GPT-SoVITS-VC 本身带有 WebUI，但因为我希望在自己的前端页面中同时使用情感分析和声音转换，所以我选择通过调用 Python 函数的方式来实现。

因为懒得自己写，所以我直接魔改了 vc_webui.py（其实只是把 Gradio 界面对应的代码删了）， 相当于 copy 了 Gradio 界面中“开始推理”按钮所对应的函数。

## References
1. [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)
2. [huangxu1991/GPT-SoVITS-VC](https://github.com/huangxu1991/GPT-SoVITS-VC)

## Contributors

This project exists thanks to all the people who contribute.

<a href="https://github.com/squarezhong/SUSTech-HUM040-Voice-Changer/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=squarezhong/SUSTech-HUM040-Voice-Changer" />
</a>

## License
Apache License 2.0
