# Prompt:
# Buggy Code: A provided TensorFlow script has errors (e.g., dimension mismatches, incorrect loss functions). Debug and fix the code.


# 1. Buggy Code Example:
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(28, 28)),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)


# 2. Fixed Code with Explanation:

# Correct input shape (flattened image: 28x28 = 784)
x_train_flat = x_train.reshape(-1, 28 * 28)
x_test_flat = x_test.reshape(-1, 28 * 28)

# Convert labels to one-hot encoded vectors
from tensorflow.keras.utils import to_categorical
y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

# Define the model with correct input/output format
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')  # softmax for multi-class
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train_flat, y_train_cat, epochs=3, validation_split=0.1)


# 3. Explanation of Fixes:
  # Input Shape Fixed: Flattened 28x28 images into 784-length vectors.
  # Loss Function Updated: From mse to categorical_crossentropy, appropriate for multi-class classification.
  # Softmax Output: Added to match classification task expectations.




