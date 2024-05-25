import librosa
import soundfile
import os,glob,pickle
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

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

with open('emotion_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
        
def predict_emotion(file):
    feature = extract_feature(file, mfcc=True, chroma=True, mel=True)
    feature = feature.reshape(1, -1)
    predicted_emotion = model.predict(feature)[0]
    return predicted_emotion
    
# following code is used to train the model
if __name__ == '__main__':
    
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

    observed_emotions = ['calm','happy','sad','angry']

    def load_data(test_size=0.2):
        x,y=[],[]
        for file in glob.glob("../speech-emotion-recognition-ravdess-data/*/*.wav"):
            file_name = os.path.basename(file)
            emotion = emotions[file_name.split("-")[2]]
            if emotion not in  observed_emotions:
                continue
            feature = extract_feature(file,mfcc=True,chroma=True,mel=True)
            x.append(feature)
            y.append(emotion)
        return train_test_split(np.array(x),y,test_size=test_size,random_state=9)

    x_train,x_test,y_train,y_test = load_data(0.25)
    
    # 定义MLP
    model = MLPClassifier(alpha=0.02,
                        batch_size=256,
                        activation='relu',
                        solver='adam',
                        hidden_layer_sizes=(300,),
                        learning_rate='adaptive',
                        max_iter=300)

    # 定义参数网格
    param_grid = {
        'alpha': [0.01, 0.02, 0.05],
        'hidden_layer_sizes': [(50,), (100,), (300,)],
        'activation': ['relu', 'tanh'],
        'solver': ['adam', 'sgd', 'lbfgs'],
        'learning_rate': ['constant', 'adaptive'],
        'max_iter': [100, 200, 300]
    }

    # 创建GridSearchCV对象
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, verbose=1, n_jobs=-1)
    grid_search.fit(x_train, y_train)

    # 输出最佳参数和最佳模型的得分
    print("Best parameters found: ", grid_search.best_params_)
    print("Best cross-validation score: {:.2f}".format(grid_search.best_score_))

    # 使用最佳参数的模型对测试集进行预测
    best_model = grid_search.best_estimator_
    test_accuracy = best_model.score(x_test, y_test)
    print("Test set accuracy of best model: {:.2f}".format(test_accuracy))
    with open('emotion_model.pkl', 'wb') as model_file:
        pickle.dump(best_model, model_file)
