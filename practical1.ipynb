import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

# Generate Dummy Data
data = {'feature1': [1, 2, 3, 4, 5], 'feature2': [5, 4, 3, 2, 1], 'label': [2, 4, 6, 8, 10]}
df = pd.DataFrame(data)

# Normalize Data
X = df[['feature1', 'feature2']].values
y = df['label'].values

# Visualize Data
plt.scatter(df['feature1'], df['label'])
plt.title('Feature vs Label')
plt.show()

# TensorFlow Model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(X.shape[1],)),
    tf.keras.layers.Dense(1)
])

# Compile and Train
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.fit(X, y, epochs=10, verbose=1)

# Evaluate
loss, mae = model.evaluate(X, y)
print(f"Loss: {loss}, MAE: {mae}")

# Save Model
model.save('simple_model.h5')
