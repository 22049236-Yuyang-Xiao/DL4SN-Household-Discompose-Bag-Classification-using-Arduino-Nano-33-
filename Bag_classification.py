import os, cv2

import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Input, Lambda, Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf

def img_process(f_path):
    data = []
    IMG_SIZE = 224
    categories = ["Garbage", "Paper","Plastic"]
    for category in categories:
        path_link = os.path.join(f_path, category)
        label = categories.index(category)
        print(label)
        for image in os.listdir(path_link):
            try:
                img_array = cv2.imread(os.path.join(path_link, image), cv2.IMREAD_COLOR)
                resized_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                data.append([resized_array, label])
            except Exception as e:
                print(e)
    print(data)
    return data

# def eye_status(f_path):
#     labels = ['Closed', 'Open']
#     IMG_SIZE = 330
#     data = []
#     for i in labels:
#         path = os.path.join(f_path, i)
#         class_num = labels.index(i)
#         class_num +=2
#         print(class_num)
#         for img in os.listdir(path):
#             try:
#                 img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_COLOR)
#                 resized_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
#                 data.append([resized_array, class_num])
#             except Exception as e:
#                 print(e)
#     return data
#
#

face_cas_path="/Users/zoro/Documents/GitHub/casa0018/cw/image_cut/haarcascade_frontalface_default.xml"
f_path="/Users/zoro/Desktop/Bag"
eye_cas = "/Users/zoro/Documents/GitHub/casa0018/cw/image_cut/haarcascade.xml"



def append_data():
    x = []
    y = []
    integrate = img_process(f_path)
    for feature, label in np.array(integrate):
        x.append(feature)
        y.append(label)
    X = np.array(x)
    X = X.reshape(-1, 224, 224, 3)

    label_bin = LabelBinarizer()
    y = label_bin.fit_transform(y)
    Y = np.array(y)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=42, test_size=0.3)

    print('x and y are: ')

    print(X_train,Y_train)


    train_generator = ImageDataGenerator(rescale=1/255, zoom_range=0.2, horizontal_flip=True, rotation_range=30)
    test_generator = ImageDataGenerator(rescale=1/255)

    train_generator = train_generator.flow(np.array(X_train), Y_train, shuffle=False)
    test_generator = test_generator.flow(np.array(X_test), Y_test, shuffle=False)

    model = Sequential()

    model.add(Conv2D(256, (3, 3), activation="relu", input_shape=X_train.shape[1:]))
    model.add(MaxPooling2D(2, 2))

    model.add(Conv2D(128, (3, 3), activation="relu"))
    model.add(MaxPooling2D(2, 2))

    model.add(Conv2D(64, (3, 3), activation="relu"))
    model.add(MaxPooling2D(2, 2))

    model.add(Conv2D(32, (3, 3), activation="relu"))
    model.add(MaxPooling2D(2, 2))

    model.add(Flatten())
    model.add(Dropout(0.5))

    model.add(Dense(64, activation="relu"))
    model.add(Dense(3, activation="softmax"))

    model.compile(loss="categorical_crossentropy", metrics=["accuracy"], optimizer="adam")

    model.summary()

    history = model.fit(train_generator, epochs=30, validation_data=test_generator, shuffle=True, validation_steps=len(test_generator))

    accuracy = history.history['accuracy']
    val_accuracy = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(len(accuracy))

    plt.plot(epochs, accuracy, "b", label="trainning accuracy")
    plt.plot(epochs, val_accuracy, "r", label="validation accuracy")
    plt.legend()
    plt.show()

    plt.plot(epochs, loss, "b", label="trainning loss")
    plt.plot(epochs, val_loss, "r", label="validation loss")
    plt.legend()
    plt.show()

    return

append_data()

