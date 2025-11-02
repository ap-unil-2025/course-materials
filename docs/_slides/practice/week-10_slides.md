---
marp: true
paginate: true
header: "Session 10: Neural Networks Without the Hype"
footer: "Anna Smirnova, November 17, 2025"
style: |
  section {
    font-size: 22px;
  }
  section.lead {
    font-size: 28px;
    background: #003aff;
    color: white;
  }
  section.lead footer, section.lead header, section.lead h1, section.lead h2, section.lead h3 {
    color: white;
  }
---

<!-- _class: lead -->

# Neural Networks Without the Hype

**Practical guide to your first deep learning model**

---

# Today's Plan

**15 min:** What actually happens in a neural network
**30 min:** Build and train your first neural net

**Tools:**
- Keras (part of TensorFlow)
- Simple, high-level API
- Works like sklearn but for deep learning

**Goal:** Working neural network, not magic

---

# Neural Network in 3 Bullets

1. **Stack of layers** that transform inputs → outputs
2. **Weights** that get adjusted during training
3. **Loss function** that tells you how wrong you are

**That's it.**

Everything else is optimization details.

---

# The Keras Recipe

```python
from tensorflow import keras

# 1. Define architecture
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(10,)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

# 2. Compile (choose optimizer and loss)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 3. Train
model.fit(X_train, y_train, epochs=10, validation_split=0.2)

# 4. Predict
y_pred = model.predict(X_test)
```

**Familiar pattern if you know sklearn!**

---

# Dense Layer: The Building Block

```python
keras.layers.Dense(units=64, activation='relu')
```

**What it does:**
- Takes input
- Multiplies by weights (learned during training)
- Adds bias
- Applies activation function

**Parameters:**
- `units`: How many neurons (output size)
- `activation`: Nonlinearity ('relu', 'sigmoid', 'tanh', etc.)

**First layer needs `input_shape`, others figure it out automatically**

---

# Common Architecture Patterns

**Binary Classification** (spam/not spam, pass/fail):
```python
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(features,)),
    keras.layers.Dense(1, activation='sigmoid')  # Output 0-1
])
model.compile(loss='binary_crossentropy', metrics=['accuracy'])
```

**Multi-class Classification** (iris species, digit recognition):
```python
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(features,)),
    keras.layers.Dense(num_classes, activation='softmax')  # Output probabilities
])
model.compile(loss='categorical_crossentropy', metrics=['accuracy'])
```

**Regression** (price prediction):
```python
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(features,)),
    keras.layers.Dense(1)  # No activation for regression
])
model.compile(loss='mse', metrics=['mae'])
```

---

# Common Error #1: Wrong Loss Function

```python
# ❌ WRONG - Binary classification with wrong loss
model.compile(loss='mse', ...)  # MSE is for regression!

# ✅ RIGHT
model.compile(loss='binary_crossentropy', ...)
```

**Cheat sheet:**
- Binary classification → `binary_crossentropy`
- Multi-class → `categorical_crossentropy`  or `sparse_categorical_crossentropy`
- Regression → `mse` or `mae`

---

# Common Error #2: Wrong Output Activation

```python
# ❌ WRONG - Regression with sigmoid (outputs 0-1 only)
Dense(1, activation='sigmoid')  # Can't predict prices!

# ✅ RIGHT - No activation for regression
Dense(1)  # Can output any number
```

**Cheat sheet:**
- Binary classification → `sigmoid` (last layer)
- Multi-class → `softmax` (last layer)
- Regression → no activation (last layer)

---

# Common Error #3: Data Shape Issues

```python
# ❌ WRONG - Missing input_shape
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu'),  # How many inputs?
    ...
])

# ✅ RIGHT - Specify input shape in first layer
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(10,)),
    ...
])
```

**Or use Input layer explicitly:**
```python
model = keras.Sequential([
    keras.layers.Input(shape=(10,)),
    keras.layers.Dense(64, activation='relu'),
    ...
])
```

---

# Training: What Those Parameters Mean

```python
model.fit(
    X_train, y_train,
    epochs=10,           # How many times to see entire dataset
    batch_size=32,       # How many samples per weight update
    validation_split=0.2 # Use 20% of training data for validation
)
```

**Typical values:**
- `epochs`: 10-100 (more if underfitting, less if overfitting)
- `batch_size`: 32, 64, or 128 (bigger = faster but less stable)
- `validation_split`: 0.1-0.2 (to monitor overfitting)

---

# Monitoring Training

```python
history = model.fit(X_train, y_train, epochs=50, validation_split=0.2)

# Plot training vs validation loss
import matplotlib.pyplot as plt
plt.plot(history.history['loss'], label='Training')
plt.plot(history.history['val_loss'], label='Validation')
plt.legend()
plt.show()
```

**What to look for:**
- Both decreasing → Good!
- Training ↓, Validation ↑ → Overfitting
- Both flat → Underfitting (need more complex model)

---

# Overfitting Solutions

**1. Early Stopping**
```python
from tensorflow.keras.callbacks import EarlyStopping

early_stop = EarlyStopping(monitor='val_loss', patience=5)
model.fit(X_train, y_train, epochs=100, callbacks=[early_stop])
```

**2. Dropout**
```python
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dropout(0.5),  # Randomly drop 50% of neurons during training
    keras.layers.Dense(1, activation='sigmoid')
])
```

**3. Reduce Model Size**
- Fewer layers or fewer neurons per layer

---

# Debugging: Model Won't Learn

**Loss not decreasing:**
- Learning rate too high/low → Try different optimizer or `learning_rate=0.001`
- Wrong loss function → Check you're using right loss for task
- Data not normalized → Neural nets love scaled data!

**Accuracy stuck at baseline:**
- Binary: 50% → Model guessing randomly
- Check data labels (are they balanced?)
- Model too simple → Add more layers/neurons

**NaN loss:**
- Learning rate too high → Reduce it
- Data has NaN/Inf values → Clean your data!

---

# Data Normalization Matters!

```python
# ❌ Without normalization - slow training
X_train = [[2000, 3, 10], [1500, 2, 5], ...]  # Different scales!

# ✅ With normalization - faster, better performance
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model.fit(X_train_scaled, y_train, ...)
```

**Always normalize for neural networks!**

---

# Quick Reference: Model Building

```python
# 1. Import
from tensorflow import keras

# 2. Build
model = keras.Sequential([
    keras.layers.Input(shape=(n_features,)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(output_size, activation=output_activation)
])

# 3. Compile
model.compile(optimizer='adam', loss=your_loss, metrics=['accuracy'])

# 4. Train
model.fit(X_train, y_train, epochs=20, validation_split=0.2)

# 5. Evaluate
model.evaluate(X_test, y_test)
```

---

# Pro Tips

**1. Start Simple**
- 1-2 hidden layers with 32-64 neurons
- Get it working, THEN add complexity

**2. Use Callbacks**
```python
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

callbacks = [
    EarlyStopping(patience=10),
    ModelCheckpoint('best_model.h5', save_best_only=True)
]
model.fit(..., callbacks=callbacks)
```

**3. Compare to sklearn First**
- If a simple sklearn model works well, you might not need deep learning!

---

<!-- _class: lead -->

# Let's Build Your First Neural Net!

**We'll predict something together**

**Questions before we code?**
