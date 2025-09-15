---
layout: assignment
title: "Problem Set Week 11: Advanced Machine Learning"
assignment_number: 111
due_date: 2025-12-01 23:59:00
difficulty: "Advanced"
estimated_time: "6-7 hours"
github_classroom_url: "https://classroom.github.com/a/nM5qR7pT-ps-week11"
topics:
  - "Reinforcement learning"
  - "Natural language processing"
  - "Computer vision"
  - "Time series analysis"
  - "Ensemble methods"
status: "active"
description: "Explore cutting-edge ML techniques and build sophisticated AI systems"
---

# Problem Set 11: Advanced Machine Learning Techniques

This week we explore advanced topics that power modern AI applications!

## Exercise 1: Reinforcement Learning - Game AI 🎮

Build an AI that learns to play games through trial and error!

### Part A: Q-Learning Implementation (30 points)
```python
import numpy as np

class QLearningAgent:
    def __init__(self, state_space, action_space, learning_rate=0.1, 
                 discount_factor=0.95, epsilon=0.1):
        self.state_space = state_space
        self.action_space = action_space
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon
        self.q_table = np.zeros((state_space, action_space))
    
    def choose_action(self, state):
        """
        Epsilon-greedy action selection:
        - Explore with probability epsilon
        - Exploit with probability 1-epsilon
        """
        # TODO: Implement epsilon-greedy
        pass
    
    def update(self, state, action, reward, next_state):
        """
        Q-learning update rule:
        Q(s,a) = Q(s,a) + α[r + γ*max(Q(s',a')) - Q(s,a)]
        """
        # TODO: Implement Q-learning update
        pass
    
    def train(self, env, episodes=1000):
        """Train agent in environment"""
        # TODO: Implement training loop
        pass
```

### Part B: Deep Q-Network (DQN) (35 points)
Scale to complex state spaces with neural networks:

```python
class DQN:
    def __init__(self, state_dim, action_dim, hidden_dim=128):
        self.state_dim = state_dim
        self.action_dim = action_dim
        # Main network
        self.q_network = self.build_network(hidden_dim)
        # Target network for stability
        self.target_network = self.build_network(hidden_dim)
        self.memory = ReplayBuffer(capacity=10000)
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01
    
    def build_network(self, hidden_dim):
        """Build neural network for Q-value approximation"""
        # TODO: Create NN architecture
        pass
    
    def remember(self, state, action, reward, next_state, done):
        """Store experience in replay buffer"""
        # TODO: Add to memory
        pass
    
    def replay(self, batch_size=32):
        """
        Experience replay:
        1. Sample random batch from memory
        2. Calculate target Q-values
        3. Train network on batch
        """
        # TODO: Implement experience replay
        pass
    
    def update_target_network(self):
        """Periodically update target network"""
        # TODO: Copy weights
        pass
```

### Part C: Environment - Grid World Game (35 points)
Create a game environment for testing:

```python
class GridWorld:
    def __init__(self, size=10):
        self.size = size
        self.reset()
    
    def reset(self):
        """
        Initialize game:
        - Player position
        - Goal position
        - Obstacles
        - Rewards
        """
        # TODO: Setup environment
        pass
    
    def step(self, action):
        """
        Execute action and return:
        - next_state
        - reward
        - done
        - info
        """
        # TODO: Implement game logic
        pass
    
    def render(self):
        """Visualize current game state"""
        # TODO: ASCII or matplotlib visualization
        pass

def train_and_evaluate(agent, env):
    """
    Train agent and show:
    - Learning curves
    - Optimal policy visualization
    - Performance metrics
    """
    # TODO: Complete training pipeline
    pass
```

## Exercise 2: Natural Language Processing 📝

Build advanced NLP models!

### Part A: Word Embeddings from Scratch (30 points)
Implement Word2Vec:

```python
class Word2Vec:
    def __init__(self, vocab_size, embedding_dim=100, window_size=5):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.window_size = window_size
        # Initialize embeddings randomly
        self.embeddings = np.random.randn(vocab_size, embedding_dim) * 0.01
        self.word_to_idx = {}
        self.idx_to_word = {}
    
    def create_training_data(self, sentences):
        """
        Create skip-gram training pairs:
        (center_word, context_word)
        """
        # TODO: Generate training pairs
        pass
    
    def train_skip_gram(self, training_data, epochs=100):
        """
        Skip-gram with negative sampling:
        1. Forward pass
        2. Calculate loss
        3. Backpropagate
        """
        # TODO: Implement skip-gram
        pass
    
    def most_similar(self, word, n=5):
        """Find most similar words using cosine similarity"""
        # TODO: Calculate similarities
        pass
    
    def analogy(self, word1, word2, word3):
        """
        Solve analogies: word1 - word2 + word3
        e.g., king - man + woman = queen
        """
        # TODO: Implement word arithmetic
        pass
```

### Part B: Transformer Architecture (40 points)
Build a transformer from scratch:

```python
class TransformerBlock:
    def __init__(self, d_model=512, n_heads=8, d_ff=2048):
        self.d_model = d_model
        self.n_heads = n_heads
        self.attention = MultiHeadAttention(d_model, n_heads)
        self.norm1 = LayerNorm(d_model)
        self.norm2 = LayerNorm(d_model)
        self.feed_forward = FeedForward(d_model, d_ff)
    
    def forward(self, x, mask=None):
        """
        Transformer block:
        1. Multi-head attention
        2. Add & normalize
        3. Feed-forward
        4. Add & normalize
        """
        # TODO: Implement transformer block
        pass

class MultiHeadAttention:
    def __init__(self, d_model, n_heads):
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads
        
        self.W_q = np.random.randn(d_model, d_model) * 0.01
        self.W_k = np.random.randn(d_model, d_model) * 0.01
        self.W_v = np.random.randn(d_model, d_model) * 0.01
        self.W_o = np.random.randn(d_model, d_model) * 0.01
    
    def forward(self, query, key, value, mask=None):
        """
        Multi-head attention mechanism:
        1. Project to Q, K, V
        2. Split into heads
        3. Apply attention
        4. Concatenate heads
        5. Final projection
        """
        # TODO: Implement multi-head attention
        pass
    
    def scaled_dot_product_attention(self, Q, K, V, mask=None):
        """
        Attention(Q,K,V) = softmax(QK^T/√d_k)V
        """
        # TODO: Implement attention
        pass
```

### Part C: Named Entity Recognition (30 points)
Build NER system:

```python
class NERTagger:
    def __init__(self, vocab_size, tag_size, hidden_dim=256):
        """
        BiLSTM-CRF for sequence labeling:
        - Bidirectional LSTM
        - CRF layer for constraints
        """
        self.vocab_size = vocab_size
        self.tag_size = tag_size
        self.bilstm = None
        self.crf = None
    
    def build_model(self):
        """Build BiLSTM-CRF architecture"""
        # TODO: Create model
        pass
    
    def viterbi_decode(self, emissions, transition_matrix):
        """
        Find best tag sequence using Viterbi algorithm
        """
        # TODO: Implement Viterbi
        pass
    
    def train(self, sentences, tags):
        """Train on labeled data"""
        # TODO: Training pipeline
        pass
    
    def predict(self, sentence):
        """
        Predict entity tags:
        - PERSON, LOCATION, ORGANIZATION, etc.
        """
        # TODO: Inference
        pass
```

## Exercise 3: Computer Vision - Object Detection 👁️

Build an object detection system!

### Part A: Sliding Window Detector (25 points)
```python
class SlidingWindowDetector:
    def __init__(self, classifier, window_sizes, stride=8):
        self.classifier = classifier
        self.window_sizes = window_sizes
        self.stride = stride
    
    def detect(self, image):
        """
        Detect objects using sliding windows:
        1. Slide windows at multiple scales
        2. Classify each window
        3. Apply non-maximum suppression
        """
        detections = []
        # TODO: Implement sliding window
        return detections
    
    def non_maximum_suppression(self, boxes, scores, threshold=0.5):
        """
        Remove overlapping detections:
        1. Sort by confidence
        2. Remove high-overlap boxes
        """
        # TODO: Implement NMS
        pass
    
    def compute_iou(self, box1, box2):
        """Calculate Intersection over Union"""
        # TODO: Calculate IoU
        pass
```

### Part B: Region Proposal Network (35 points)
Simplified R-CNN:

```python
class RegionProposalNetwork:
    def __init__(self, feature_dim, num_anchors=9):
        self.feature_dim = feature_dim
        self.num_anchors = num_anchors
        # Classification head
        self.cls_head = None
        # Regression head
        self.reg_head = None
    
    def generate_anchors(self, feature_map_size):
        """
        Generate anchor boxes:
        - Multiple scales
        - Multiple aspect ratios
        """
        # TODO: Create anchors
        pass
    
    def forward(self, feature_map):
        """
        For each anchor:
        - Classify as object/background
        - Regress bounding box offsets
        """
        # TODO: RPN forward pass
        pass
    
    def decode_predictions(self, cls_scores, reg_offsets, anchors):
        """Convert network output to bounding boxes"""
        # TODO: Decode predictions
        pass
```

### Part C: Image Segmentation (40 points)
Pixel-level classification:

```python
class UNet:
    def __init__(self, input_channels=3, num_classes=21):
        """
        U-Net architecture for segmentation:
        - Encoder (downsampling)
        - Decoder (upsampling)
        - Skip connections
        """
        self.encoder_layers = []
        self.decoder_layers = []
    
    def encoder_block(self, in_channels, out_channels):
        """Convolutional block with pooling"""
        # TODO: Build encoder block
        pass
    
    def decoder_block(self, in_channels, out_channels):
        """Upsampling block with skip connection"""
        # TODO: Build decoder block
        pass
    
    def forward(self, x):
        """
        Forward pass:
        1. Encode to features
        2. Decode to segmentation map
        3. Pixel-wise classification
        """
        # TODO: U-Net forward pass
        pass
    
    def dice_loss(self, pred, target):
        """Dice coefficient loss for segmentation"""
        # TODO: Implement Dice loss
        pass
```

## Exercise 4: Time Series Forecasting 📈

Predict future values from historical data!

### Part A: ARIMA from Scratch (30 points)
```python
class ARIMA:
    def __init__(self, p, d, q):
        """
        ARIMA(p,d,q) model:
        p: autoregressive order
        d: differencing order
        q: moving average order
        """
        self.p = p
        self.d = d
        self.q = q
        self.ar_params = None
        self.ma_params = None
    
    def difference(self, series, order):
        """Apply differencing to make series stationary"""
        # TODO: Implement differencing
        pass
    
    def fit(self, series):
        """
        Fit ARIMA model:
        1. Difference series
        2. Estimate AR parameters
        3. Estimate MA parameters
        """
        # TODO: Fit model
        pass
    
    def forecast(self, steps):
        """Forecast future values"""
        # TODO: Generate forecasts
        pass
    
    def check_stationarity(self, series):
        """Augmented Dickey-Fuller test"""
        # TODO: Test for stationarity
        pass
```

### Part B: Prophet-like Forecasting (35 points)
Decomposition-based forecasting:

```python
class TimeSeriesDecomposer:
    def __init__(self):
        self.trend = None
        self.seasonal = None
        self.residual = None
    
    def decompose(self, series, period):
        """
        Decompose time series:
        - Trend component
        - Seasonal component
        - Residual component
        """
        # TODO: STL decomposition
        pass
    
    def fit_trend(self, series):
        """Fit trend using polynomial or spline"""
        # TODO: Trend fitting
        pass
    
    def fit_seasonality(self, series, period):
        """Extract seasonal patterns"""
        # TODO: Fourier analysis
        pass
    
    def forecast(self, steps):
        """Combine components for forecast"""
        # TODO: Additive/multiplicative forecast
        pass
```

### Part C: LSTM for Time Series (35 points)
```python
class TimeSeriesLSTM:
    def __init__(self, input_dim, hidden_dim, output_dim, seq_length):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.seq_length = seq_length
        self.lstm = None
    
    def create_sequences(self, data):
        """
        Create sequences for LSTM:
        - Input: [t-n, ..., t-1]
        - Output: [t]
        """
        # TODO: Sequence creation
        pass
    
    def build_model(self):
        """Build LSTM architecture"""
        # TODO: Create model
        pass
    
    def train(self, data, epochs=100):
        """Train with early stopping"""
        # TODO: Training loop
        pass
    
    def multi_step_forecast(self, initial_sequence, steps):
        """
        Multi-step ahead forecasting:
        - Recursive prediction
        - Direct prediction
        - Seq2seq approach
        """
        # TODO: Multi-step forecasting
        pass
```

## Real-World Capstone Project 🌍

Choose ONE comprehensive project:

### Option A: Autonomous Trading Bot
```python
class TradingBot:
    def __init__(self):
        self.rl_agent = None  # RL for decisions
        self.predictor = None  # Time series forecasting
        self.risk_manager = None  # Risk management
    
    def train(self, historical_data):
        """Train all components"""
        pass
    
    def trade(self, current_market):
        """Make trading decisions"""
        pass
```

### Option B: Medical Diagnosis System
```python
class MedicalDiagnosisAI:
    def __init__(self):
        self.image_analyzer = None  # CNN for X-rays
        self.nlp_processor = None  # Process medical text
        self.predictor = None  # Disease prediction
    
    def diagnose(self, patient_data):
        """Comprehensive diagnosis"""
        pass
```

### Option C: Smart Content Moderator
```python
class ContentModerator:
    def __init__(self):
        self.text_classifier = None  # Toxic text detection
        self.image_classifier = None  # Inappropriate images
        self.video_analyzer = None  # Video content analysis
    
    def moderate(self, content):
        """Multi-modal content moderation"""
        pass
```

## Bonus Challenges 🌟

### Challenge 1: Meta-Learning (30 points)
```python
class MAML:
    """Model-Agnostic Meta-Learning"""
    def meta_train(self, tasks):
        """Learn to learn quickly"""
        pass
```

### Challenge 2: Federated Learning (30 points)
```python
class FederatedLearning:
    """Train on distributed data"""
    def aggregate_models(self, client_models):
        """Combine models privately"""
        pass
```

### Challenge 3: Explainable AI (30 points)
```python
class SHAP:
    """SHapley Additive exPlanations"""
    def explain_prediction(self, model, instance):
        """Feature importance explanation"""
        pass
```

## Submission Requirements

Your submission should include:
1. `reinforcement_learning.py` - RL implementations
2. `nlp_models.py` - NLP algorithms
3. `computer_vision.py` - CV models
4. `time_series.py` - Forecasting methods
5. `capstone_project/` - Your chosen project
6. `experiments.ipynb` - All experiments
7. `README.md` - Detailed analysis

## Grading Rubric

- **Algorithm Implementation (35%)**: Correct, efficient code
- **Experimental Results (25%)**: Thorough testing
- **Capstone Project (25%)**: Complete application
- **Innovation (15%)**: Creative solutions

## Tips for Success

1. **Modularize Code**: Build reusable components
2. **Test Incrementally**: Verify each part works
3. **Visualize Results**: Plots help understanding
4. **Document Assumptions**: Explain design choices
5. **Benchmark Performance**: Compare to baselines

## Resources

- [Sutton & Barto RL Book](http://incompleteideas.net/book/the-book.html)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [YOLO Object Detection](https://pjreddie.com/darknet/yolo/)
- [Time Series Forecasting](https://otexts.com/fpp3/)

## Fun Facts 🤓

- DeepMind's AlphaGo used RL to beat world Go champion
- GPT-3 has 175 billion parameters
- BERT revolutionized NLP in 2018
- U-Net was originally for biomedical imaging
- Prophet was developed by Facebook for business forecasting

Remember: These are the techniques that power modern AI - master them and you can build anything! 🚀