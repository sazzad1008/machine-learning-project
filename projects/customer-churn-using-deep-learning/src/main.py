"""
Python entrypoint scaffold generated from notebook: customer churn using deep learning.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: customer churn using deep learning.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# from  matplotlib import pyplot as plt
# import pandas as pd
# %matplotlib inline
# import numpy as np
#
# Cell 2
# df=pd.read_csv('customer_churn.csv')
# df.head()
#
# Cell 3
# df.dtypes
#
# Cell 4
# df.drop('customerID',axis='columns',inplace=True)
#
# Cell 5
# df[pd.to_numeric(df.TotalCharges,errors='coerce').isnull()]
#
# Cell 6
# df.iloc[488].TotalCharges
#
# Cell 7
# df[df.TotalCharges!=' '].shape
#
# Cell 8
# df5=df[df.TotalCharges!=' ']
#
# Cell 9
# df5.TotalCharges=pd.to_numeric(df5.TotalCharges)
# df5.dtypes
#
# Cell 10
# tenure_yes=df5[df5.Churn=='Yes'].tenure
# tenure_no=df5[df5.Churn=='No'].tenure
# plt.hist([tenure_yes,tenure_no],color=['green','red'])
#
# Cell 11
# def unique(df):
#     for col in df:
#         df[col].dtypes=='object'
#         print(f'{col}:{df[col].unique()}')
#
# Cell 12
# unique(df5)
#
# Cell 13
# df5.replace('No internet service','No',inplace=True)
# df5.replace('No phone service','No',inplace=True)
#
# Cell 14
# unique(df5)
#
# Cell 15
# yes_no_columns = ['Partner','Dependents','PhoneService','MultipleLines','OnlineSecurity','OnlineBackup',
#                   'DeviceProtection','TechSupport','StreamingTV','StreamingMovies','PaperlessBilling','Churn']
# for col in df5:
#     df5.replace({'Yes':1,'No':0},inplace=True)
#
# Cell 16
# unique(df5)
#
# Cell 17
# df5.gender.replace({'Female':0,'Male':0},inplace=True)
#
# Cell 18
# df5
#
# Cell 19
# df6 = pd.get_dummies(data=df5, columns=['InternetService','Contract','PaymentMethod'])
# df6
#
# Cell 20
# cols_to_scale = ['tenure','MonthlyCharges','TotalCharges']
# from sklearn.preprocessing import MinMaxScaler
# scalar=MinMaxScaler()
# df6[cols_to_scale]=scalar.fit_transform(df6[cols_to_scale])
#
# Cell 21
#
#
# Cell 22
# unique(df6)
#
# Cell 23
# x=df6.drop('Churn',axis='columns')
# y=df6.Churn.astype(np.float32)
#
# Cell 24
# from sklearn.model_selection import train_test_split
# X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.5,stratify=y,random_state=5)
#
# Cell 25
# import tensorflow as tf
# from tensorflow import keras
# from sklearn.metrics import confusion_matrix,classification_report
#
# Cell 26
# def ANN(xtrain,ytrain,xtest,ytest,loss):
#     model=keras.Sequential([
#         keras.layers.Dense(26,input_dim=26,activation='relu'),
#         keras.layers.Dense(15,activation='relu'),
#         keras.layers.Dense(1, activation='sigmoid')
#     ])
#     model.compile(optimizer='adam',loss=loss,metrics=['accuracy'])
#     model.fit(xtrain,ytrain,epochs=100)
#     print(model.evaluate(xtest,ytest))
#     ypred=model.predict(xtest)
#     ypred=np.around(ypred)
#     print('classification \n',classification_report(ytest,ypred))
#     return ypred
#
# Cell 27
# ANN(xtrain,xte,xtest,ytest,'binary_crossentropy')
#
# Cell 28
# def ANNp(X_train, y_train, X_test, y_test, loss, weights):
#     model = keras.Sequential([
#         keras.layers.Dense(26, input_shape=(26,1), activation='relu'),
#         keras.layers.Dense(10, activation='relu'),
#         keras.layers.Dense(1, activation='sigmoid')
#     ])
#
#
#     model.compile(optimizer='adam', loss=loss, metrics=['accuracy'])
#
#     if weights == -1:
#         model.fit(X_train, y_train, epochs=100)
#     else:
#         model.fit(X_train, y_train, epochs=100, class_weight = weights)
#
#     print(model.evaluate(X_test, y_test))
#
#     y_preds = model.predict(X_test)
#     y_preds = np.round(y_preds)
#
#     print("Classification Report: \n", classification_report(y_test, y_preds))
#
#     return y_preds
#
# Cell 29
# ANNp(X_train, y_train, X_test, y_test, 'binary_crossentropy', -1)
#
# Cell 30
# X_train.shape
#
# Cell 31
# ytrain.shape
#
# Cell 32
# modelp= keras.Sequential([
#         keras.layers.Dense(26, input_shape=(26,1), activation='relu'),
#         keras.layers.Dense(10, activation='relu'),
#         keras.layers.Dense(1, activation='sigmoid')
#     ])
#
# Cell 33
# modelp.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# modelp.fit(X_train,y_train,epochs=100)
#
# Cell 34
# ypredss=modelp.predict(X_test.resh)
#
# Cell 35
# X_test.shape
#
# Cell 36
# modelp.predict(X_test)
#
# Cell 37
# ypredss=np.round(ypredss)
# ypredss.reshape(3516,)
#
# Cell 38
# classification_report(y_test.array,ypredss)
#
# Cell 39
# y_test.array
#
# Cell 40
# ypredss
#
# Cell 41
# X_test.values
#
# Cell 42
#
#
# Cell 43
# y_test.shape
#
# Cell 44
# ypredss.reshape(3516,)
#
# Cell 45
# pp='rifath damra'
#
# Cell 46
# for i in range(50):
#     print(pp)
#
#
# Cell 47
# pip install imbalanced-learn
#
# Cell 48
#
#
