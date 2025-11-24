# Iris Classification: Model Comparison

## Research Question
Which classification model performs best for Iris species:
Random Forest, K-Nearest Neighbors, or Logistic Regression?

## Setup

### Option 1: Conda (Recommended for Nuvolos)
```bash
# Create environment
conda env create -f environment.yml
conda activate iris-project
```

### Option 2: pip + venv (Local Python)
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### Option 3: uv (Fast Alternative)
```bash
# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Expected output: Accuracy comparison between three models.

## Project Structure

```
iris-classification/
├── main.py              # Main entry point
├── src/                 # Source code
│   ├── __init__.py
│   ├── data_loader.py   # Data loading/preprocessing
│   ├── models.py        # Model training
│   └── evaluation.py    # Evaluation metrics
├── data/
│   └── raw/             # Original data (Iris loaded from sklearn)
├── results/             # Output plots and metrics
├── notebooks/           # Jupyter notebooks for exploration
└── environment.yml      # Dependencies (conda)
```

## Results

Based on our experiments:
- **Logistic Regression**: 0.967 accuracy ⭐
- **Random Forest**: 0.933 accuracy
- **K-Nearest Neighbors**: 0.933 accuracy
- **Winner**: Logistic Regression

Interesting finding: The simpler linear model (Logistic Regression) outperforms
the more complex models, suggesting that Iris classes are linearly separable.

## Requirements

- Python 3.11
- scikit-learn
- pandas
- matplotlib
- seaborn

## Reproducibility

All random operations use `random_state=31` for reproducibility.
Running the code multiple times will produce identical results.
