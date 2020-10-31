import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense,Conv2D,MaxPool2D,Flatten,Dropout
from keras.optimizers import RMSprop
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ReduceLROnPlateau
from csv import DictReader


help(__import__)
import importlib

from  keras.callbacks import Callback

sns.set(style='white', context='notebook', palette='deep')

train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")


Y_train=train["label"]
X_train=train.drop(labels = ["label"],axis = 1)

X_train=X_train/255
test=test/255

X_train.shape
X_train=X_train.values.reshape(-1,28,28,1)
Y_train = to_categorical(Y_train, num_classes = 10)

Y_train.shape


x_train,x_val,y_train,y_val=train_test_split(X_train, Y_train, test_size = 0.15,
                                             random_state = 2)

plt.imshow(x_train[0][:,:,0],cmap="gray_r")


model=Sequential()
model.add(Conv2D(input_shape=(28,28,1),filters=32,kernel_size=(5,5),activation="relu"))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Conv2D(filters=32,kernel_size=(5,5),activation="relu"))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Conv2D(filters=64,kernel_size=(3,3),activation="relu"))
model.add(MaxPool2D(pool_size=(2,2), strides=(2,2)))
model.add(Conv2D(filters=96,kernel_size=(1,1),activation="relu"))
model.add(MaxPool2D(pool_size=(1,1), strides=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(256, activation = "relu"))
model.add(Dropout(0.5))
model.add(Dense(10, activation = "softmax"))
model.summary()

optimizer = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
model.compile(optimizer = optimizer,loss = "categorical_crossentropy",metrics=["accuracy"])

learn_rate= ReduceLROnPlateau(monitor='val_acc',patience=3,verbose=1,factor=0.5,min_lr=0.00001)


datagen = ImageDataGenerator(
        featurewise_center=False,  # set input mean to 0 over the dataset
        samplewise_center=False,  # set each sample mean to 0
        featurewise_std_normalization=False,  # divide inputs by std of the dataset
        samplewise_std_normalization=False,  # divide each input by its std
        zca_whitening=False,  # apply ZCA whitening
        rotation_range=10,  # randomly rotate images in the range (degrees, 0 to 180)
        zoom_range = 0.1, # Randomly zoom image 
        width_shift_range=0.1,  # randomly shift images horizontally (fraction of total width)
        height_shift_range=0.1,  # randomly shift images vertically (fraction of total height)
        horizontal_flip=False,  # randomly flip images
        vertical_flip=False)  # randomly flip images
datagen.fit(X_train)


        
        
history = LossHistory()

h = model.fit_generator(datagen.flow(X_train,Y_train, batch_size=86),
                              epochs = 2, validation_data = (x_val,y_val),
                              verbose = 1,steps_per_epoch=X_train.shape[0] // 86
                              , callbacks=[learn_rate])

print(len(history.losses))

model.evaluate()

X_train.shape

plt.plot(h.history['loss'])
plt.plot(h.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epochs')
plt.legend(['train', 'test'])
plt.show()

plt.plot(h.history['acc'])
plt.plot(h.history['val_acc'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epochs')
plt.legend(['train', 'test'])
plt.show()


test=test.values.reshape(-1,28,28,1)
pred=model.predict(test)

pred.shape

pred1=np.argmax(pred,axis=1)
pred1.shape
pred1=pred1.tolist()

l=[]
for i in range(1,28001):
    l.append(i)


df=pd.DataFrame(data={"ImageId":l,"Label":pred1})
df.to_csv("submit2.csv",sep=',',index=False)
