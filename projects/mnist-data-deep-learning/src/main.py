"""
Python entrypoint scaffold generated from notebook: mnist data deep learning.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: mnist data deep learning.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import tensorflow as tf
# from tensorflow import keras
# import matplotlib.pyplot as plt
# %matplotlib inline
# import numpy as np
# from tensorflow.keras.callbacks import TensorBoard
# from time import time
#
# Cell 2
# (xtrain,ytrain),(xtest,ytest)=keras.datasets.mnist.load_data()
#
# Cell 3
#
#
# Cell 4
# xtrain[0]
#
# Cell 5
# xflat=xtrain.reshape(len(xtrain),28*28)
# xflat[0]
#
#
# Cell 6
# xflat=xtrain.reshape(len(xtrain),28*28)
#
# Cell 7
# xflatest=xtest.reshape(len(xtest),28*28)
#
# Cell 8
# model = keras.Sequential([
#     keras.layers.Flatten(input_shape=(28, 28)),
#     keras.layers.Dense(100, activation='relu'),
#     keras.layers.Dense(10, activation='sigmoid')
# ])
#
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
# tf_callback=TensorBoard(log_dir='Logs/{}'.format(time()))
# model.fit(xtrain, ytrain, epochs=5,callbacks=[tf_callback])
#
# Cell 9
# model.evaluate(xtest,ytest)
#
# Cell 10
# yp=model.predict(xtest)
# yp[0]
#
# Cell 11
# plt.matshow(xtest[0])
#
# Cell 12
# ytest[0]
#
# Cell 13
# yplabel=[np.argmax(i) for  i in yp]
#
# Cell 14
#
#
# Cell 15
# cm=tf.math.confusion_matrix(labels=ytest,predictions=yplabel)
# cm
#
# Cell 16
# import seaborn as sn
# plt.figure(figsize=(10,7))
# sn.heatmap(cm,annot=True,fmt='d')
#
# Cell 17
#
#
# Cell 18
# %load_ext tensorboard
# %tensorboard --logdir Logs/fit
#
# Cell 19
#
#
