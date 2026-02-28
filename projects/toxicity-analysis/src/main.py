"""
Python entrypoint scaffold generated from notebook: toxicity analysis.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: toxicity analysis.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import os
# import pandas as pd
# import tensorflow as tf
# import numpy as np
#
# Cell 2
# df=pd.read_csv('toxic train.csv')
# df.head()
#
# Cell 3
# x=df.comment_text
# y=df[df.columns[2:]].values
#
# Cell 4
# y
#
# Cell 5
# from tensorflow.keras.layers import TextVectorization
#
# Cell 6
# vectorize=TextVectorization(max_tokens=20000,output_sequence_length=180,output_mode='int')
#
# Cell 7
# vectorize.adapt(x.values)
#
# Cell 8
# vectorized_text=vectorize(x.values)
#
# Cell 9
# vectorized_text
#
# Cell 10
# dataset=tf.data.Dataset.from_tensor_slices((vectorized_text,y))
# dataset=dataset.cache()
# dataset=dataset.shuffle(16000)
# dataset=dataset.batch(16)
# dataset=dataset.prefetch(8)
#
# Cell 11
# dataset.as_numpy_iterator().next()
#
# Cell 12
#
# train = dataset.take(int(len(dataset)*.7))
# val = dataset.skip(int(len(dataset)*.7)).take(int(len(dataset)*.2))
# test = dataset.skip(int(len(dataset)*.9)).take(int(len(dataset)*.1))
#
# Cell 13
#
#
