# Assignment Difficulty Guide

## Complexity Levels for Intro Programming Course

### Week 1-3: Basics (Git & Python Fundamentals)
**Appropriate Difficulty:**
- Simple functions with clear input/output
- Basic control flow (if/else, loops)
- Working with strings and lists
- No complex algorithms

**Time Estimate:** 2-4 hours per assignment

**Example Problems:**
- Temperature converter
- Calculate average of list
- Count words in text
- Simple calculator

### Week 4-6: Intermediate Python
**Appropriate Difficulty:**
- Multiple functions working together
- Basic file I/O
- Simple classes and objects
- Basic error handling

**Time Estimate:** 4-5 hours per assignment

**Example Problems:**
- Contact manager with file storage
- Simple game (tic-tac-toe, hangman)
- Data analysis with dictionaries
- Basic web scraping

### Week 7-9: Introduction to ML
**Appropriate Difficulty:**
- Use existing libraries (sklearn)
- Implement simple algorithms from scratch
- Basic data preprocessing
- Simple visualizations

**Time Estimate:** 5-6 hours per assignment

**Example Problems:**
- Linear regression using sklearn
- Implement k-NN from scratch (simplified)
- Basic k-means clustering
- Simple classification on clean datasets

### Week 10-12: Advanced Topics
**Appropriate Difficulty:**
- Combine multiple concepts
- Use more advanced libraries
- Simple optimization problems
- Basic parallel processing

**Time Estimate:** 6-7 hours per assignment

**Example Problems:**
- Simple neural network with TensorFlow/Keras
- Basic web application
- Data pipeline with pandas
- Simple performance optimization

## Adjusting Difficulty

### To Make Easier:
1. **Provide more starter code**
   - Give function signatures
   - Include helper functions
   - Provide templates

2. **Break into smaller steps**
   - More detailed instructions
   - Intermediate checkpoints
   - Partial credit opportunities

3. **Simplify requirements**
   - Remove edge cases
   - Use simpler datasets
   - Reduce feature requirements

### To Make Harder:
1. **Add constraints**
   - No external libraries
   - Performance requirements
   - Memory limitations

2. **Add features**
   - Error handling
   - Input validation
   - Extended functionality

3. **Require analysis**
   - Performance comparison
   - Written explanations
   - Test case design

## GitHub Classroom Setup

### For Each Assignment:

1. **Create Template Repository**
   ```
   assignment-week-X/
   ├── README.md           # Instructions
   ├── requirements.txt    # Dependencies
   ├── test_assignment.py  # Automated tests
   ├── starter_code.py     # Template files
   └── .github/
       └── classroom/
           └── autograding.json
   ```

2. **Autograding Configuration**
   - Each test worth specific points
   - Total should equal 100
   - Set reasonable timeouts
   - Clear test names

3. **Provide Clear Rubric**
   - 70% Automated tests
   - 20% Code quality
   - 10% Documentation

## Recommended Assignment Progression

### Weeks 1-2: Git & Setup
- **Assignment 1**: Git basics (no coding)

### Weeks 3-4: Python Basics
- **Assignment 3**: Control flow & functions
- **Assignment 4**: Data structures

### Weeks 5-6: Intermediate Python
- **Assignment 5**: File I/O and exceptions
- **Assignment 6**: Classes and OOP

### Week 7: Midterm Project
- Combine weeks 1-6 concepts

### Weeks 8-9: Data Science Intro
- **Assignment 8**: NumPy and Pandas basics
- **Assignment 9**: Data visualization

### Weeks 10-11: ML Basics
- **Assignment 10**: Supervised learning with sklearn
- **Assignment 11**: Unsupervised learning basics

### Week 12: Web/API
- **Assignment 12**: Simple REST API or web scraping

### Weeks 13-14: Final Project
- Student choice from provided options

## Common Pitfalls to Avoid

1. **Too much math** - Focus on programming, not mathematical proofs
2. **Unclear specifications** - Be very explicit about requirements
3. **Hidden test cases** - Show most test cases to students
4. **Too many concepts at once** - Introduce gradually
5. **Assuming prior knowledge** - Start from basics

## Sample Difficulty Progression

### Easy (Weeks 1-4)
```python
def add_numbers(a, b):
    """Add two numbers"""
    return a + b
```

### Medium (Weeks 5-8)
```python
class BankAccount:
    """Simple bank account with deposits/withdrawals"""
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
```

### Harder (Weeks 9-12)
```python
def k_nearest_neighbors(X_train, y_train, X_test, k=3):
    """Implement k-NN classifier"""
    predictions = []
    for test_point in X_test:
        distances = calculate_distances(test_point, X_train)
        nearest = find_k_nearest(distances, k)
        predictions.append(majority_vote(nearest, y_train))
    return predictions
```

## Testing Strategy

### Unit Tests
- Test individual functions
- Check edge cases
- Verify type handling

### Integration Tests
- Test function interactions
- Check file I/O
- Verify data flow

### Performance Tests (Advanced Only)
- Time limits for algorithms
- Memory usage checks
- Scalability tests

## Support Materials

For each assignment provide:
1. **Video walkthrough** of similar problem
2. **Office hours** before due date
3. **Discussion forum** for questions
4. **Sample solutions** (after deadline)
5. **Common mistakes** document