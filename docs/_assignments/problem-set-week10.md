---
layout: assignment
title: "Problem Set Week 10: Deep Learning Primer"
assignment_number: 110
due_date: 2025-11-24 23:59:00
difficulty: "Advanced"
estimated_time: "6-7 hours"
github_classroom_url: "https://classroom.github.com/a/wK4pL8nR-ps-week10"
topics:
  - "Neural networks"
  - "Backpropagation"
  - "CNNs"
  - "RNNs"
  - "TensorFlow/PyTorch"
status: "active"
description: "Build neural networks from scratch and explore deep learning fundamentals"
---

# Problem Set 10: Deep Learning - Neural Networks from Scratch

Welcome to deep learning! This week you'll build neural networks from the ground up and then use modern frameworks.

## Exercise 1: Neural Network from Scratch 🧠

Build a complete neural network without any ML libraries!

### Part A: Forward Propagation (25 points)
```python
import numpy as np

class Layer:
    def __init__(self, input_size, output_size, activation='relu'):
        self.weights = np.random.randn(input_size, output_size) * 0.01
        self.bias = np.zeros((1, output_size))
        self.activation = activation
        self.input = None
        self.output = None
    
    def forward(self, X):
        """
        Compute forward pass:
        1. Linear transformation: Z = XW + b
        2. Apply activation function
        """
        # TODO: Implement forward propagation
        # TODO: Store input for backprop
        pass
    
    def activate(self, Z):
        """Apply activation function"""
        if self.activation == 'relu':
            # TODO: ReLU activation
            pass
        elif self.activation == 'sigmoid':
            # TODO: Sigmoid activation
            pass
        elif self.activation == 'softmax':
            # TODO: Softmax for output layer
            pass

class NeuralNetwork:
    def __init__(self, layer_sizes):
        """
        layer_sizes: list of layer dimensions
        e.g., [784, 128, 64, 10] for MNIST
        """
        self.layers = []
        # TODO: Initialize layers
        pass
    
    def forward(self, X):
        """Forward pass through entire network"""
        # TODO: Pass through all layers
        pass
```

### Part B: Backpropagation (35 points)
Implement the chain rule for gradient computation:

```python
class Layer:
    def backward(self, d_output, learning_rate):
        """
        Backpropagate gradients:
        1. Compute gradient of activation
        2. Compute gradients for weights and bias
        3. Pass gradient to previous layer
        """
        # TODO: Implement backpropagation
        # TODO: Update weights and bias
        pass
    
    def activation_derivative(self, Z):
        """Compute derivative of activation function"""
        if self.activation == 'relu':
            # TODO: ReLU derivative
            pass
        elif self.activation == 'sigmoid':
            # TODO: Sigmoid derivative
            pass

class NeuralNetwork:
    def backward(self, X, y, learning_rate=0.01):
        """
        Backpropagate error through network:
        1. Compute loss gradient
        2. Propagate through layers in reverse
        """
        # TODO: Compute initial gradient
        # TODO: Backprop through all layers
        pass
    
    def train(self, X, y, epochs=100, batch_size=32):
        """
        Train network with mini-batch gradient descent
        """
        # TODO: Implement training loop
        # TODO: Add batch processing
        pass
```

### Part C: Loss Functions & Optimizers (20 points)
```python
class LossFunctions:
    @staticmethod
    def cross_entropy(y_true, y_pred):
        """Multi-class cross-entropy loss"""
        # TODO: Implement loss
        pass
    
    @staticmethod
    def mse(y_true, y_pred):
        """Mean squared error loss"""
        # TODO: Implement loss
        pass

class Optimizers:
    class SGD:
        def __init__(self, learning_rate=0.01, momentum=0.9):
            self.lr = learning_rate
            self.momentum = momentum
            self.velocity = {}
        
        def update(self, params, gradients):
            """SGD with momentum"""
            # TODO: Implement momentum update
            pass
    
    class Adam:
        def __init__(self, learning_rate=0.001, beta1=0.9, beta2=0.999):
            self.lr = learning_rate
            self.beta1 = beta1
            self.beta2 = beta2
            self.m = {}  # First moment
            self.v = {}  # Second moment
            self.t = 0   # Time step
        
        def update(self, params, gradients):
            """Adam optimizer"""
            # TODO: Implement Adam update
            pass
```

### Part D: Training on MNIST (20 points)
Apply your network to digit recognition:

```python
def train_mnist_classifier():
    """
    1. Load MNIST data (simplified version)
    2. Preprocess (normalize, flatten)
    3. Build network [784, 128, 64, 10]
    4. Train and evaluate
    5. Visualize learning curves
    """
    # TODO: Complete MNIST training
    pass
```

## Exercise 2: Convolutional Neural Network (CNN) 🖼️

Build a CNN for image classification!

### Part A: Convolution & Pooling Layers (35 points)
```python
class Conv2D:
    def __init__(self, n_filters, filter_size, stride=1, padding=0):
        self.n_filters = n_filters
        self.filter_size = filter_size
        self.stride = stride
        self.padding = padding
        self.filters = None
        self.bias = None
    
    def forward(self, X):
        """
        2D Convolution:
        1. Pad input if needed
        2. Slide filters over input
        3. Compute dot products
        """
        # TODO: Implement convolution
        pass
    
    def backward(self, d_output):
        """Backprop through convolution"""
        # TODO: Compute gradients
        pass

class MaxPool2D:
    def __init__(self, pool_size=2, stride=2):
        self.pool_size = pool_size
        self.stride = stride
        self.max_indices = None
    
    def forward(self, X):
        """
        Max pooling:
        1. Divide input into pools
        2. Take maximum in each pool
        3. Store indices for backprop
        """
        # TODO: Implement max pooling
        pass
    
    def backward(self, d_output):
        """Route gradients to max locations"""
        # TODO: Implement backprop
        pass
```

### Part B: CNN Architecture (30 points)
Build a complete CNN:

```python
class SimpleCNN:
    def __init__(self, input_shape, n_classes):
        """
        Architecture:
        Conv(32) -> ReLU -> MaxPool ->
        Conv(64) -> ReLU -> MaxPool ->
        Flatten -> Dense(128) -> Dense(n_classes)
        """
        self.layers = []
        # TODO: Build CNN architecture
        pass
    
    def forward(self, X):
        """Forward pass through CNN"""
        # TODO: Pass through all layers
        pass
    
    def train(self, X_train, y_train, X_val, y_val):
        """Train CNN with data augmentation"""
        # TODO: Implement training
        # TODO: Add data augmentation
        pass
```

### Part C: Image Data Augmentation (35 points)
```python
class ImageAugmentation:
    @staticmethod
    def random_rotation(image, max_angle=30):
        """Randomly rotate image"""
        # TODO: Implement rotation
        pass
    
    @staticmethod
    def random_flip(image, horizontal=True, vertical=False):
        """Randomly flip image"""
        # TODO: Implement flipping
        pass
    
    @staticmethod
    def random_crop(image, crop_size):
        """Random crop and resize"""
        # TODO: Implement cropping
        pass
    
    @staticmethod
    def random_brightness(image, max_delta=0.2):
        """Adjust brightness randomly"""
        # TODO: Implement brightness adjustment
        pass
```

## Exercise 3: Recurrent Neural Network (RNN) 📝

Build RNNs for sequence modeling!

### Part A: Vanilla RNN (30 points)
```python
class RNNCell:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        # Weights for input to hidden
        self.W_ih = np.random.randn(input_size, hidden_size) * 0.01
        # Weights for hidden to hidden
        self.W_hh = np.random.randn(hidden_size, hidden_size) * 0.01
        self.b_h = np.zeros((1, hidden_size))
        self.hidden_state = None
    
    def forward(self, x_t, h_prev):
        """
        Single RNN step:
        h_t = tanh(W_ih @ x_t + W_hh @ h_prev + b_h)
        """
        # TODO: Implement RNN cell
        pass
    
    def backward(self, d_h_next, d_output):
        """Backprop through time (BPTT)"""
        # TODO: Implement BPTT
        pass

class RNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.rnn_cell = RNNCell(input_size, hidden_size)
        self.output_layer = Layer(hidden_size, output_size)
    
    def forward(self, X_sequence):
        """Process entire sequence"""
        # TODO: Unroll RNN over time
        pass
```

### Part B: LSTM Implementation (35 points)
Long Short-Term Memory for better gradient flow:

```python
class LSTMCell:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        
        # Gates: input, forget, output, candidate
        self.W_i = self._init_weights()  # Input gate
        self.W_f = self._init_weights()  # Forget gate
        self.W_o = self._init_weights()  # Output gate
        self.W_c = self._init_weights()  # Candidate
        
        self.cell_state = None
        self.hidden_state = None
    
    def forward(self, x_t, h_prev, c_prev):
        """
        LSTM forward pass with gates:
        1. Forget gate: what to forget
        2. Input gate: what to store
        3. Update cell state
        4. Output gate: what to output
        """
        # TODO: Implement LSTM gates
        # TODO: Update cell and hidden states
        pass
```

### Part C: Text Generation (35 points)
Build a character-level language model:

```python
class TextGenerator:
    def __init__(self, vocab_size, hidden_size=128):
        self.vocab_size = vocab_size
        self.rnn = RNN(vocab_size, hidden_size, vocab_size)
        self.char_to_idx = {}
        self.idx_to_char = {}
    
    def train_on_text(self, text, epochs=50):
        """
        Train on text data:
        1. Create character vocabulary
        2. Convert text to sequences
        3. Train RNN to predict next character
        """
        # TODO: Implement training
        pass
    
    def generate_text(self, seed_text, length=100, temperature=1.0):
        """
        Generate new text:
        1. Start with seed
        2. Predict next character
        3. Sample from predictions
        4. Feed back as input
        """
        # TODO: Implement generation
        pass
    
    def sample_with_temperature(self, predictions, temperature):
        """Control randomness in generation"""
        # TODO: Implement temperature sampling
        pass
```

## Exercise 4: Modern Deep Learning with TensorFlow/PyTorch 🚀

Now use real frameworks!

### Part A: Transfer Learning (30 points)
```python
import tensorflow as tf
# or import torch

def transfer_learning_classifier(n_classes):
    """
    1. Load pre-trained model (ResNet, VGG, etc.)
    2. Freeze base layers
    3. Add custom classification head
    4. Fine-tune on new dataset
    """
    # TODO: Implement transfer learning
    pass

def fine_tune_model(model, dataset, unfreeze_at=100):
    """
    Progressive unfreezing:
    1. Train only new layers
    2. Gradually unfreeze and fine-tune
    """
    # TODO: Implement fine-tuning
    pass
```

### Part B: Custom Training Loop (35 points)
```python
class CustomTrainer:
    def __init__(self, model, optimizer, loss_fn):
        self.model = model
        self.optimizer = optimizer
        self.loss_fn = loss_fn
        self.train_loss = []
        self.val_loss = []
    
    @tf.function  # or @torch.jit.script
    def train_step(self, x, y):
        """Single training step with gradient tape"""
        # TODO: Implement custom training
        pass
    
    def train(self, train_data, val_data, epochs):
        """
        Custom training loop with:
        - Learning rate scheduling
        - Early stopping
        - Model checkpointing
        - TensorBoard logging
        """
        # TODO: Implement training loop
        pass
```

### Part C: Model Deployment (35 points)
```python
class ModelServer:
    def __init__(self, model_path):
        self.model = self.load_model(model_path)
    
    def preprocess(self, input_data):
        """Prepare input for model"""
        # TODO: Implement preprocessing
        pass
    
    def predict(self, input_data):
        """Make prediction with confidence scores"""
        # TODO: Implement inference
        pass
    
    def export_for_production(self):
        """
        Export model for deployment:
        - TensorFlow Lite (mobile)
        - ONNX (cross-platform)
        - TensorFlow.js (browser)
        """
        # TODO: Export model
        pass
```

## Real-World Project: Build Your Own GPT 🤖

Create a mini language model from scratch!

```python
class MiniGPT:
    def __init__(self, vocab_size, d_model=512, n_heads=8, n_layers=6):
        """
        Simplified transformer architecture:
        - Multi-head attention
        - Position encodings
        - Feed-forward networks
        """
        self.embedding = None
        self.position_encoding = None
        self.transformer_blocks = []
        # TODO: Build architecture
    
    def attention(self, Q, K, V, mask=None):
        """Scaled dot-product attention"""
        # TODO: Implement attention
        pass
    
    def multi_head_attention(self, x, n_heads):
        """Split into multiple attention heads"""
        # TODO: Implement multi-head
        pass
    
    def train_on_corpus(self, text_corpus):
        """Train on text data"""
        # TODO: Implement training
        pass
    
    def generate(self, prompt, max_length=100):
        """Generate text from prompt"""
        # TODO: Implement generation
        pass
```

## Bonus Challenges 🌟

### Challenge 1: GAN Implementation (30 points)
```python
class SimpleGAN:
    def __init__(self):
        self.generator = self.build_generator()
        self.discriminator = self.build_discriminator()
    
    def train(self, real_data):
        """
        GAN training:
        1. Train discriminator on real/fake
        2. Train generator to fool discriminator
        """
        # TODO: Implement GAN training
        pass
```

### Challenge 2: Attention Visualization (30 points)
```python
def visualize_attention(model, input_sequence):
    """
    Create attention heatmaps showing:
    - What model focuses on
    - Head-wise attention patterns
    """
    # TODO: Extract and visualize attention
    pass
```

### Challenge 3: Neural Architecture Search (30 points)
```python
def search_architecture(dataset, search_space):
    """
    Automatically find optimal architecture:
    - Random search
    - Evolutionary algorithms
    - Reinforcement learning
    """
    # TODO: Implement NAS
    pass
```

## Submission Requirements

Your submission should include:
1. `neural_network.py` - NN from scratch
2. `cnn.py` - CNN implementation
3. `rnn.py` - RNN/LSTM implementation
4. `modern_dl.py` - TensorFlow/PyTorch code
5. `experiments.ipynb` - All experiments
6. `models/` - Saved trained models
7. `README.md` - Architecture descriptions and results

## Grading Rubric

- **From-Scratch Implementation (40%)**: Working NN without libraries
- **Framework Usage (25%)**: Effective use of TF/PyTorch
- **Model Performance (20%)**: Achieving good accuracy
- **Code Quality (15%)**: Clean, efficient, documented

## Tips for Success

1. **Start Small**: Test on XOR problem before MNIST
2. **Check Gradients**: Verify with numerical gradients
3. **Initialize Carefully**: Bad initialization = no learning
4. **Monitor Training**: Watch for exploding/vanishing gradients
5. **Use Batch Norm**: Helps with deep networks

## Common Pitfalls

- Not normalizing inputs (crucial for NNs)
- Wrong matrix dimensions in backprop
- Forgetting to shuffle training data
- Learning rate too high/low
- Not using GPU when available

## Resources

- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)
- [CS231n Stanford Course](http://cs231n.stanford.edu/)
- [Distill.pub Visualizations](https://distill.pub/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)

## Fun Facts 🤓

- The first neural network was built in 1958 (Perceptron)
- Backpropagation was discovered independently 3+ times
- Modern GPUs can do 100+ TFLOPS (trillion operations/second)
- The largest models have >1 trillion parameters
- Deep learning was almost abandoned in the 1990s ("AI Winter")

Remember: Deep learning is just function approximation with extra steps - but those steps can do magic! ✨