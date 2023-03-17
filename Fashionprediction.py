 Importing the necessary libraries
import tensorflow as tf

# Loading the Fashion-MNIST dataset downloadable from tensorflow
data = tf.keras.datasets.fashion_mnist.load_data()
(X_train, y_train), (X_test, y_test) = data

# Normalizing the pixel value for the maximum allowes, in this case it will be 8-bit
X_train = X_train / 255.0
X_test = X_test / 255.0
# Defining a CNN model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation="relu", input_shape=(28,28,1)),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Conv2D(64, (3,3), activation="relu"),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Conv2D(128, (3,3), activation="relu"),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])

# Compiling the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Training the model on the Fashion-MNIST dataset
model.fit(X_train.reshape(-1,28,28,1), y_train, epochs=10, validation_data=(X_test.reshape(-1,28,28,1), y_test))
import numpy as np
import matplotlib.pyplot as plt

# Using a random image from the test set
index = np.random.randint(0, len(X_test))
image = X_test[index].reshape(28,28)

# Making a prediction using the trained model
prediction = model.predict(image.reshape(1,28,28,1))[0]
category = np.argmax(prediction)

# Ploting the image and prediction result
fig, ax = plt.subplots()
ax.imshow(image, cmap="gray")
ax.set_title(f"Predicted category: {category}")
