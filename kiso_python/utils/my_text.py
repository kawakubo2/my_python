# -*- coding: utf-8 -*-

import pickle, tfidf
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.models import model_from_json

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
tf.compat.v1.keras.backend.set_session(tf.compat.v1.Session(config=config))

# TF-IDFの辞書を読み込む
tfidf.load_dic('text\genre-tfidf.dic')

# Kerasのモデルを定義して重みデータを読み込む
nb_classes = 4
model = Sequential()
model.add(Dense(512, activation='relu',input_shape=(29416,))) # 本来は52800
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(nb_classes, activation='softmax'))
model.compile(
    loss='categorical_crossentropy',
    optimizer=RMSprop(),
    metrics=['binary_accuracy'])
model.load_weights('text\genre-model.hdf5')

# テキストを指定して判定
def check_genre(text):
    LABELS = ['スポーツ', 'IT', '映画', 'ライフ']
    # TF-IDFのベクトルに変換
    data = tfidf.calc_text(text)
    # MLPで遅く
    pre = model.predict(np.array([data]))[0]
    n = pre.argmax()
    print(LABELS[n], "(", pre[n], ")")
    return LABELS[n], float(pre[n]), int(n)