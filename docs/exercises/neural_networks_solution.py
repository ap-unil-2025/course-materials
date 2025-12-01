"""
Neural Networks Solution
Week 10 - Advanced Programming 2025

Complete solution with all TODOs and bonus challenges implemented.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification, load_iris, load_breast_cancer

# Keras imports
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Sequential
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras import regularizers

print(f"✅ TensorFlow version: {tf.__version__}")

# Set random seed for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

print("=" * 60)
print("PART 1: BINARY CLASSIFICATION - Cancer Detection")
print("=" * 60)

# Load breast cancer dataset
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target  # 0 = malignant, 1 = benign

print(f"Dataset shape: {X.shape}")
print(f"Classes: {np.unique(y)}")
print(f"Class distribution: {np.bincount(y)}")

# SOLUTION 1: Split the data (80/20 train/test split)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

# SOLUTION 2: Scale the features
# Neural networks work better with scaled data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Feature mean before scaling: {X_train.mean().mean():.2f}")
print(f"Feature mean after scaling: {X_train_scaled.mean():.2f}")

# SOLUTION 3: Build a binary classification model
# Binary classification: output layer has 1 neuron with sigmoid activation
model_binary = Sequential([
    layers.Dense(32, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    layers.Dense(16, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Binary: 1 neuron, sigmoid activation
])

print("\n📐 Model Architecture:")
model_binary.summary()

# SOLUTION 4: Compile the model
# Binary classification uses binary_crossentropy loss
model_binary.compile(
    optimizer='adam',
    loss='binary_crossentropy',  # For binary classification
    metrics=['accuracy']
)

# SOLUTION 5: Train the model
print("\n🏋️ Training binary classification model...")
history_binary = model_binary.fit(
    X_train_scaled, y_train,
    epochs=50,
    validation_split=0.2,
    verbose=0  # Set to 1 to see progress
)

print("✅ Training complete!")

# SOLUTION 6: Evaluate on test set
test_loss, test_accuracy = model_binary.evaluate(X_test_scaled, y_test, verbose=0)
print(f"\n📊 Test Loss: {test_loss:.4f}")
print(f"📊 Test Accuracy: {test_accuracy:.4f}")

# SOLUTION 7: Plot training history
def plot_history(history, title="Training History"):
    """Plot training and validation metrics."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    # Plot loss
    ax1.plot(history.history['loss'], label='Training Loss')
    ax1.plot(history.history['val_loss'], label='Validation Loss')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss')
    ax1.set_title(f'{title} - Loss')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Plot accuracy
    ax2.plot(history.history['accuracy'], label='Training Accuracy')
    ax2.plot(history.history['val_accuracy'], label='Validation Accuracy')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Accuracy')
    ax2.set_title(f'{title} - Accuracy')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('binary_classification_history.png', dpi=100, bbox_inches='tight')
    print("📈 Plot saved as 'binary_classification_history.png'")
    plt.show()

plot_history(history_binary, "Binary Classification Training")


print("\n" + "=" * 60)
print("PART 2: MULTI-CLASS CLASSIFICATION - Iris Flowers")
print("=" * 60)

# Load iris dataset
iris = load_iris()
X_iris = iris.data
y_iris = iris.target  # 0, 1, 2 (three species)

print(f"Dataset shape: {X_iris.shape}")
print(f"Classes: {np.unique(y_iris)}")
print(f"Number of classes: {len(np.unique(y_iris))}")
print(f"Class names: {iris.target_names}")

# Split and scale
X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(
    X_iris, y_iris, test_size=0.2, random_state=42
)

scaler_iris = StandardScaler()
X_train_iris_scaled = scaler_iris.fit_transform(X_train_iris)
X_test_iris_scaled = scaler_iris.transform(X_test_iris)

# SOLUTION 8: Convert labels to one-hot encoding
# For categorical_crossentropy, we need one-hot encoding
# [0, 1, 2] -> [[1,0,0], [0,1,0], [0,0,1]]
y_train_iris_onehot = keras.utils.to_categorical(y_train_iris, num_classes=3)
y_test_iris_onehot = keras.utils.to_categorical(y_test_iris, num_classes=3)

print(f"Original label shape: {y_train_iris.shape}")
print(f"One-hot label shape: {y_train_iris_onehot.shape}")
print(f"Example original: {y_train_iris[0]}")
print(f"Example one-hot: {y_train_iris_onehot[0]}")

# SOLUTION 9: Build a multi-class classification model
# Multi-class: output layer has 3 neurons with softmax activation
model_multiclass = Sequential([
    layers.Dense(16, activation='relu', input_shape=(4,)),
    layers.Dense(8, activation='relu'),
    layers.Dense(3, activation='softmax')  # Multi-class: 3 neurons, softmax activation
])

print("\n📐 Model Architecture:")
model_multiclass.summary()

# SOLUTION 10: Compile the model
# Multi-class with one-hot encoding uses categorical_crossentropy
model_multiclass.compile(
    optimizer='adam',
    loss='categorical_crossentropy',  # For multi-class with one-hot encoding
    metrics=['accuracy']
)

# SOLUTION 11: Train the model
print("\n🏋️ Training multi-class classification model...")
history_multiclass = model_multiclass.fit(
    X_train_iris_scaled, y_train_iris_onehot,
    epochs=100,
    validation_split=0.2,
    verbose=0
)

print("✅ Training complete!")

# SOLUTION 12: Evaluate
test_loss_iris, test_accuracy_iris = model_multiclass.evaluate(
    X_test_iris_scaled, y_test_iris_onehot, verbose=0
)
print(f"\n📊 Test Loss: {test_loss_iris:.4f}")
print(f"📊 Test Accuracy: {test_accuracy_iris:.4f}")

# SOLUTION 13: Make predictions and show confusion matrix
from sklearn.metrics import confusion_matrix, classification_report

y_pred_probs = model_multiclass.predict(X_test_iris_scaled, verbose=0)
y_pred = np.argmax(y_pred_probs, axis=1)  # Convert probabilities to class labels

print("\n📈 Confusion Matrix:")
cm = confusion_matrix(y_test_iris, y_pred)
print(cm)

print("\n📋 Classification Report:")
print(classification_report(y_test_iris, y_pred, target_names=iris.target_names))

# Visualize confusion matrix
plt.figure(figsize=(8, 6))
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix - Iris Classification')
plt.colorbar()
tick_marks = np.arange(len(iris.target_names))
plt.xticks(tick_marks, iris.target_names, rotation=45)
plt.yticks(tick_marks, iris.target_names)

# Add text annotations
thresh = cm.max() / 2.
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, format(cm[i, j], 'd'),
                ha="center", va="center",
                color="white" if cm[i, j] > thresh else "black")

plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.tight_layout()
plt.savefig('iris_confusion_matrix.png', dpi=100, bbox_inches='tight')
print("📈 Confusion matrix saved as 'iris_confusion_matrix.png'")
plt.show()


print("\n" + "=" * 60)
print("PART 3: DEBUGGING CHALLENGE - Fix This Broken Model!")
print("=" * 60)

X_debug, y_debug = make_classification(
    n_samples=1000, n_features=10, n_classes=3,
    n_informative=8, n_redundant=0, random_state=42
)

X_train_debug, X_test_debug, y_train_debug, y_test_debug = train_test_split(
    X_debug, y_debug, test_size=0.2, random_state=42
)

# Show the broken model
print("🐛 BROKEN MODEL:")
broken_model = Sequential([
    layers.Dense(32, activation='relu', input_shape=(10,)),
    layers.Dense(16, activation='relu'),
    layers.Dense(3, activation='sigmoid')  # 🐛 BUG 1: Should be softmax for multi-class
])

broken_model.compile(
    optimizer='adam',
    loss='binary_crossentropy',  # 🐛 BUG 2: Should be categorical_crossentropy
    metrics=['accuracy']
)

print("\n🐛 Training broken model...")
try:
    history_debug = broken_model.fit(
        X_train_debug, y_train_debug,  # 🐛 BUG 3: y should be one-hot encoded
        epochs=20, validation_split=0.2, verbose=0
    )
    test_loss_debug, test_accuracy_debug = broken_model.evaluate(
        X_test_debug, y_test_debug, verbose=0
    )
    print(f"Test Accuracy: {test_accuracy_debug:.4f}")
    print("⚠️  The model trained but accuracy is suspiciously low!")
except Exception as e:
    print(f"❌ Error: {e}")

# SOLUTION 14: Create a FIXED version of the model
print("\n" + "=" * 60)
print("✅ FIXED MODEL:")
print("=" * 60)

fixed_model = Sequential([
    layers.Dense(32, activation='relu', input_shape=(10,)),
    layers.Dense(16, activation='relu'),
    layers.Dense(3, activation='softmax')  # ✅ FIX 1: Use softmax for multi-class
])

fixed_model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',  # ✅ FIX 2: Use categorical_crossentropy
    metrics=['accuracy']
)

# ✅ FIX 3: One-hot encode the labels
y_train_debug_fixed = keras.utils.to_categorical(y_train_debug, num_classes=3)
y_test_debug_fixed = keras.utils.to_categorical(y_test_debug, num_classes=3)

print("🏋️ Training fixed model...")
history_fixed = fixed_model.fit(
    X_train_debug, y_train_debug_fixed,
    epochs=20, validation_split=0.2, verbose=0
)

test_loss_fixed, test_accuracy_fixed = fixed_model.evaluate(
    X_test_debug, y_test_debug_fixed, verbose=0
)
print(f"✅ Fixed Model Test Accuracy: {test_accuracy_fixed:.4f}")
print(f"📈 Improvement: {(test_accuracy_fixed - test_accuracy_debug) * 100:.1f}% better!")


print("\n" + "=" * 60)
print("BONUS CHALLENGES - SOLUTIONS")
print("=" * 60)

# BONUS 1: Early Stopping
print("\n--- BONUS 1: Early Stopping ---")

def bonus_early_stopping():
    """Add early stopping to prevent overfitting."""
    early_stop = EarlyStopping(
        monitor='val_loss',
        patience=10,
        restore_best_weights=True,
        verbose=1
    )

    model = Sequential([
        layers.Dense(32, activation='relu', input_shape=(X_train_scaled.shape[1],)),
        layers.Dense(16, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    print("Training with early stopping...")
    history = model.fit(
        X_train_scaled, y_train,
        epochs=200,  # Set high, early stopping will stop us
        validation_split=0.2,
        callbacks=[early_stop],
        verbose=0
    )

    print(f"Stopped at epoch: {len(history.history['loss'])}")

    test_loss, test_acc = model.evaluate(X_test_scaled, y_test, verbose=0)
    print(f"Test accuracy: {test_acc:.4f}")

    return history

history_early = bonus_early_stopping()


# BONUS 2: Learning Rate Experiments
print("\n--- BONUS 2: Learning Rate Experiments ---")

def bonus_learning_rates():
    """Compare different learning rates."""
    learning_rates = [0.001, 0.01, 0.1]
    results = []

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    for idx, lr in enumerate(learning_rates):
        print(f"Testing learning rate: {lr}")

        model = Sequential([
            layers.Dense(32, activation='relu', input_shape=(X_train_scaled.shape[1],)),
            layers.Dense(16, activation='relu'),
            layers.Dense(1, activation='sigmoid')
        ])

        model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=lr),
            loss='binary_crossentropy',
            metrics=['accuracy']
        )

        history = model.fit(
            X_train_scaled, y_train,
            epochs=50,
            validation_split=0.2,
            verbose=0
        )

        test_loss, test_acc = model.evaluate(X_test_scaled, y_test, verbose=0)
        results.append({'lr': lr, 'accuracy': test_acc, 'history': history})

        # Plot
        axes[idx].plot(history.history['loss'], label='Training')
        axes[idx].plot(history.history['val_loss'], label='Validation')
        axes[idx].set_title(f'LR = {lr}\nTest Acc: {test_acc:.3f}')
        axes[idx].set_xlabel('Epoch')
        axes[idx].set_ylabel('Loss')
        axes[idx].legend()
        axes[idx].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('learning_rate_comparison.png', dpi=100, bbox_inches='tight')
    print("📈 Saved as 'learning_rate_comparison.png'")
    plt.show()

    # Summary
    print("\nLearning Rate Results:")
    for r in results:
        print(f"  LR {r['lr']}: Test Accuracy = {r['accuracy']:.4f}")

    return results

lr_results = bonus_learning_rates()


# BONUS 3: Regularization
print("\n--- BONUS 3: Regularization (Dropout + L2) ---")

def bonus_regularization():
    """Add dropout and L2 regularization."""

    # Model without regularization
    model_no_reg = Sequential([
        layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
        layers.Dense(32, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])

    # Model with dropout
    model_dropout = Sequential([
        layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
        layers.Dropout(0.5),
        layers.Dense(32, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(1, activation='sigmoid')
    ])

    # Model with L2 regularization
    model_l2 = Sequential([
        layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],),
                    kernel_regularizer=regularizers.l2(0.01)),
        layers.Dense(32, activation='relu',
                    kernel_regularizer=regularizers.l2(0.01)),
        layers.Dense(1, activation='sigmoid')
    ])

    # Model with both
    model_both = Sequential([
        layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],),
                    kernel_regularizer=regularizers.l2(0.01)),
        layers.Dropout(0.3),
        layers.Dense(32, activation='relu',
                    kernel_regularizer=regularizers.l2(0.01)),
        layers.Dropout(0.3),
        layers.Dense(1, activation='sigmoid')
    ])

    models = {
        'No Regularization': model_no_reg,
        'Dropout (0.5)': model_dropout,
        'L2 Regularization': model_l2,
        'Dropout + L2': model_both
    }

    results = {}

    for name, model in models.items():
        print(f"Training: {name}")
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        history = model.fit(
            X_train_scaled, y_train,
            epochs=50,
            validation_split=0.2,
            verbose=0
        )

        test_loss, test_acc = model.evaluate(X_test_scaled, y_test, verbose=0)
        results[name] = {
            'test_acc': test_acc,
            'val_acc': history.history['val_accuracy'][-1],
            'overfitting': history.history['accuracy'][-1] - history.history['val_accuracy'][-1]
        }

    # Display results
    print("\nRegularization Results:")
    print(f"{'Method':<20} {'Test Acc':<12} {'Overfitting':<12}")
    print("-" * 45)
    for name, res in results.items():
        print(f"{name:<20} {res['test_acc']:<12.4f} {res['overfitting']:<12.4f}")

    return results

reg_results = bonus_regularization()


# BONUS 4: Architecture Search
print("\n--- BONUS 4: Architecture Search ---")

def bonus_architecture_search():
    """Try different numbers of layers and layer sizes."""
    architectures = [
        {'name': '1 Layer (16)', 'layers': [16]},
        {'name': '2 Layers (32,16)', 'layers': [32, 16]},
        {'name': '3 Layers (64,32,16)', 'layers': [64, 32, 16]},
        {'name': '2 Layers (128,64)', 'layers': [128, 64]},
        {'name': '4 Layers (128,64,32,16)', 'layers': [128, 64, 32, 16]},
    ]

    results = []

    for arch in architectures:
        print(f"Testing architecture: {arch['name']}")

        # Build model
        model = Sequential()
        model.add(layers.Dense(arch['layers'][0], activation='relu',
                              input_shape=(X_train_iris_scaled.shape[1],)))

        for units in arch['layers'][1:]:
            model.add(layers.Dense(units, activation='relu'))

        model.add(layers.Dense(3, activation='softmax'))

        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        history = model.fit(
            X_train_iris_scaled, y_train_iris_onehot,
            epochs=100,
            validation_split=0.2,
            verbose=0
        )

        test_loss, test_acc = model.evaluate(
            X_test_iris_scaled, y_test_iris_onehot, verbose=0
        )

        results.append({
            'name': arch['name'],
            'test_acc': test_acc,
            'params': model.count_params()
        })

    # Display results
    print("\nArchitecture Search Results:")
    print(f"{'Architecture':<25} {'Test Acc':<12} {'Params':<10}")
    print("-" * 50)
    for res in results:
        print(f"{res['name']:<25} {res['test_acc']:<12.4f} {res['params']:<10}")

    best = max(results, key=lambda x: x['test_acc'])
    print(f"\n🏆 Best architecture: {best['name']} with {best['test_acc']:.4f} accuracy")

    return results

arch_results = bonus_architecture_search()


# BONUS 5: Activation Function Comparison
print("\n--- BONUS 5: Activation Function Comparison ---")

def bonus_activation_comparison():
    """Compare relu, tanh, sigmoid in hidden layers."""
    activations = ['relu', 'tanh', 'sigmoid']
    results = []

    for activation in activations:
        print(f"Testing activation: {activation}")

        model = Sequential([
            layers.Dense(32, activation=activation, input_shape=(X_train_scaled.shape[1],)),
            layers.Dense(16, activation=activation),
            layers.Dense(1, activation='sigmoid')  # Output stays sigmoid for binary
        ])

        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        history = model.fit(
            X_train_scaled, y_train,
            epochs=50,
            validation_split=0.2,
            verbose=0
        )

        test_loss, test_acc = model.evaluate(X_test_scaled, y_test, verbose=0)
        results.append({
            'activation': activation,
            'test_acc': test_acc,
            'final_val_loss': history.history['val_loss'][-1]
        })

    # Display results
    print("\nActivation Function Results:")
    print(f"{'Activation':<12} {'Test Acc':<12} {'Val Loss':<12}")
    print("-" * 40)
    for res in results:
        print(f"{res['activation']:<12} {res['test_acc']:<12.4f} {res['final_val_loss']:<12.4f}")

    return results

activation_results = bonus_activation_comparison()


# BONUS 7: Save and Load Models
print("\n--- BONUS 7: Save and Load Models ---")

def bonus_save_load():
    """Save and load a model."""
    # Train a simple model
    model = Sequential([
        layers.Dense(32, activation='relu', input_shape=(X_train_iris_scaled.shape[1],)),
        layers.Dense(16, activation='relu'),
        layers.Dense(3, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train_iris_scaled, y_train_iris_onehot, epochs=50, verbose=0)

    # Get predictions before saving
    pred_before = model.predict(X_test_iris_scaled[:5], verbose=0)

    # Save the model
    model.save('best_iris_model.keras')
    print("✅ Model saved as 'best_iris_model.keras'")

    # Load the model
    loaded_model = keras.models.load_model('best_iris_model.keras')
    print("✅ Model loaded successfully")

    # Get predictions after loading
    pred_after = loaded_model.predict(X_test_iris_scaled[:5], verbose=0)

    # Verify they're identical
    if np.allclose(pred_before, pred_after):
        print("✅ Predictions match! Model saved and loaded correctly.")
    else:
        print("❌ Predictions don't match!")

    print(f"\nPredictions for first test sample:")
    print(f"  Before save: {pred_before[0]}")
    print(f"  After load:  {pred_after[0]}")

bonus_save_load()


# BONUS 11: Predict Probabilities
print("\n--- BONUS 11: Predict Probabilities ---")

def bonus_probability_analysis():
    """Analyze prediction probabilities."""
    # Get predictions
    probs = model_multiclass.predict(X_test_iris_scaled, verbose=0)

    # Get max probability for each prediction
    max_probs = np.max(probs, axis=1)
    predictions = np.argmax(probs, axis=1)

    # Find most confident
    most_confident_idx = np.argmax(max_probs)
    print(f"Most confident prediction:")
    print(f"  Sample index: {most_confident_idx}")
    print(f"  Probabilities: {probs[most_confident_idx]}")
    print(f"  Predicted class: {iris.target_names[predictions[most_confident_idx]]}")
    print(f"  True class: {iris.target_names[y_test_iris[most_confident_idx]]}")
    print(f"  Confidence: {max_probs[most_confident_idx]:.4f}")

    # Find least confident
    least_confident_idx = np.argmin(max_probs)
    print(f"\nLeast confident prediction:")
    print(f"  Sample index: {least_confident_idx}")
    print(f"  Probabilities: {probs[least_confident_idx]}")
    print(f"  Predicted class: {iris.target_names[predictions[least_confident_idx]]}")
    print(f"  True class: {iris.target_names[y_test_iris[least_confident_idx]]}")
    print(f"  Confidence: {max_probs[least_confident_idx]:.4f}")

    # Plot confidence distribution
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.hist(max_probs, bins=20, edgecolor='black')
    plt.xlabel('Maximum Probability')
    plt.ylabel('Count')
    plt.title('Distribution of Prediction Confidence')
    plt.grid(True, alpha=0.3)

    plt.subplot(1, 2, 2)
    for i in range(3):
        class_probs = probs[:, i]
        plt.hist(class_probs, bins=20, alpha=0.5, label=iris.target_names[i])
    plt.xlabel('Probability')
    plt.ylabel('Count')
    plt.title('Probability Distribution by Class')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('probability_analysis.png', dpi=100, bbox_inches='tight')
    print("\n📈 Saved as 'probability_analysis.png'")
    plt.show()

bonus_probability_analysis()


# BONUS 12: Real Dataset Challenge
print("\n--- BONUS 12: Real Dataset - Wine Quality ---")

def bonus_real_dataset():
    """Compare NN with traditional ML on a real dataset."""
    from sklearn.datasets import load_wine
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.svm import SVC

    # Load wine dataset
    wine = load_wine()
    X_wine = wine.data
    y_wine = wine.target

    X_train_w, X_test_w, y_train_w, y_test_w = train_test_split(
        X_wine, y_wine, test_size=0.2, random_state=42
    )

    # Scale data
    scaler_w = StandardScaler()
    X_train_w_scaled = scaler_w.fit_transform(X_train_w)
    X_test_w_scaled = scaler_w.transform(X_test_w)

    # Prepare for NN
    y_train_w_onehot = keras.utils.to_categorical(y_train_w, num_classes=3)
    y_test_w_onehot = keras.utils.to_categorical(y_test_w, num_classes=3)

    results = {}

    # Neural Network
    print("Training Neural Network...")
    nn_model = Sequential([
        layers.Dense(32, activation='relu', input_shape=(X_train_w_scaled.shape[1],)),
        layers.Dropout(0.3),
        layers.Dense(16, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(3, activation='softmax')
    ])
    nn_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    nn_model.fit(X_train_w_scaled, y_train_w_onehot, epochs=100, verbose=0)
    _, nn_acc = nn_model.evaluate(X_test_w_scaled, y_test_w_onehot, verbose=0)
    results['Neural Network'] = nn_acc

    # Random Forest
    print("Training Random Forest...")
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train_w_scaled, y_train_w)
    rf_acc = rf.score(X_test_w_scaled, y_test_w)
    results['Random Forest'] = rf_acc

    # SVM
    print("Training SVM...")
    svm = SVC(kernel='rbf', random_state=42)
    svm.fit(X_train_w_scaled, y_train_w)
    svm_acc = svm.score(X_test_w_scaled, y_test_w)
    results['SVM'] = svm_acc

    # Display results
    print("\nModel Comparison on Wine Dataset:")
    print(f"{'Model':<20} {'Test Accuracy':<15}")
    print("-" * 35)
    for model, acc in results.items():
        print(f"{model:<20} {acc:<15.4f}")

    best_model = max(results, key=results.get)
    print(f"\n🏆 Best model: {best_model} with {results[best_model]:.4f} accuracy")

    # Visualization
    plt.figure(figsize=(8, 5))
    models = list(results.keys())
    accuracies = list(results.values())
    colors = ['#3498db', '#2ecc71', '#e74c3c']

    plt.bar(models, accuracies, color=colors, edgecolor='black')
    plt.ylabel('Test Accuracy')
    plt.title('Model Comparison - Wine Classification')
    plt.ylim([0.8, 1.0])
    plt.grid(True, alpha=0.3, axis='y')

    for i, (model, acc) in enumerate(zip(models, accuracies)):
        plt.text(i, acc + 0.01, f'{acc:.3f}', ha='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig('model_comparison.png', dpi=100, bbox_inches='tight')
    print("📈 Saved as 'model_comparison.png'")
    plt.show()

    return results

real_dataset_results = bonus_real_dataset()


print("\n" + "=" * 60)
print("🎓 KEY TAKEAWAYS")
print("=" * 60)
print("""
1. BINARY vs MULTI-CLASS:
   Binary:      sigmoid activation, binary_crossentropy loss
   Multi-class: softmax activation, categorical_crossentropy loss

2. COMMON MISTAKES FIXED:
   ❌ Using sigmoid for multi-class → ✅ Use softmax
   ❌ Using binary_crossentropy for multi-class → ✅ Use categorical_crossentropy
   ❌ Forgetting to one-hot encode labels → ✅ Use keras.utils.to_categorical
   ❌ Not scaling features → ✅ Use StandardScaler

3. DEBUGGING WORKFLOW:
   1. Check input shape matches first layer
   2. Check output shape matches number of classes
   3. Check activation function (sigmoid vs softmax)
   4. Check loss function matches problem type
   5. Check if labels are properly encoded
   6. Scale your data!

4. REGULARIZATION TECHNIQUES:
   - Dropout (0.2-0.5) to prevent overfitting
   - L2 regularization on Dense layers
   - Early stopping to avoid overtraining
   - Batch normalization for stable training

5. HYPERPARAMETER TUNING:
   - Learning rate: 0.001 is usually a good start
   - Batch size: 32 is a good default
   - Epochs: Use early stopping instead of guessing
   - Architecture: Start simple, add complexity if needed

6. WHEN TO USE NEURAL NETWORKS:
   - Complex, non-linear patterns
   - Large datasets (>1000 samples)
   - When feature engineering is difficult

   Traditional ML (RF, SVM) often works better for:
   - Small datasets (<1000 samples)
   - Tabular data with clear features
   - When you need interpretability
""")

print("\n" + "=" * 60)
print("📊 SUMMARY OF ALL RESULTS")
print("=" * 60)

print(f"\nBinary Classification (Cancer):")
print(f"  Test Accuracy: {test_accuracy:.4f}")

print(f"\nMulti-class Classification (Iris):")
print(f"  Test Accuracy: {test_accuracy_iris:.4f}")

print(f"\nFixed Model vs Broken Model:")
print(f"  Broken: {test_accuracy_debug:.4f}")
print(f"  Fixed:  {test_accuracy_fixed:.4f}")
print(f"  Improvement: {(test_accuracy_fixed - test_accuracy_debug) * 100:.1f}%")

print("\n✅ All exercises and bonus challenges completed!")
print("📁 Generated files:")
print("   - binary_classification_history.png")
print("   - iris_confusion_matrix.png")
print("   - learning_rate_comparison.png")
print("   - probability_analysis.png")
print("   - model_comparison.png")
print("   - best_iris_model.keras")
