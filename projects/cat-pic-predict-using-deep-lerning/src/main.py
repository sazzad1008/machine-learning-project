"""
Python entrypoint scaffold generated from notebook: cat pic predict using deep lerning.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: cat pic predict using deep lerning.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import tensorflow as tf
# from tensorflow.keras import datasets, layers, models
# import matplotlib.pyplot as plt
# import numpy as np
#
# Cell 2
# (xtrain,ytrain),(xtest,ytest)=datasets.cifar10.load_data()
#
# Cell 3
# ytrain
#
# Cell 4
# ytrain=ytrain.reshape(-1,)
# ytest=ytest.reshape(-1,)
#
# Cell 5
# def plot(x,y,index):
#     plt.figure(figsize=(15,2))
#     plt.imshow(x[index])
#
# Cell 6
# plot(xtrain,ytrain,0)
#
# Cell 7
# xtrain=xtrain/255.0
# ytrain=ytrain/255.0
#
# Cell 8
# ann = models.Sequential([
#         layers.Flatten(input_shape=(32,32,3)),
#         layers.Dense(3000, activation='relu'),
#         layers.Dense(1000, activation='relu'),
#         layers.Dense(10, activation='sigmoid')
#     ])
#
# ann.compile(optimizer='SGD',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
#
# Cell 9
#
#
# Cell 10
# cnn = models.Sequential([
#     layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(32, 32, 3)),
#     layers.MaxPooling2D((2, 2)),
#
#     layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
#     layers.MaxPooling2D((2, 2)),
#
#     layers.Flatten(),
#     layers.Dense(64, activation='relu'),
#     layers.Dense(10, activation='softmax')
# ])
#
# Cell 11
# cnn.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
#
# Cell 12
# cnn.fit(xtrain,ytrain,epochs=8)
#
# Cell 13
# ypred=cnn.predict(xtest)
# ypred[:6]
#
# Cell 14
# yc=[np.argmax(d) for d in ypred]
# yc[:5]
#
# Cell 15
#
#
# Cell 16
#
#
