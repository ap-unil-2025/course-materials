---
title: "Problem Set - Week 4"
date: 2025-10-13
description: "Functions, Data Structures, and Algorithms"
---

# Problem Set 4: Functions and Data Structures

This problem set focuses on functions, lists, dictionaries, and algorithmic thinking.

## Exercise 1: Pokémon Battle Calculator 🎮
Create a module `battle_calculator.py` for Pokémon damage calculations:

### a) Damage calculator
```python
def calculate_damage(level, power, attack, defense):
    """Calculate battle damage using the official formula"""
    # Damage = ((2 * Level + 10) / 250) * (Attack/Defense) * Power + 2
    
def critical_hit(base_damage):
    """Calculate critical hit damage (1.5x)"""
    # Return modified damage
```

### b) Type effectiveness
```python
def type_multiplier(attacker_type, defender_type):
    """Return damage multiplier based on type matchup"""
    # Fire > Grass (2x), Water > Fire (2x), Grass > Water (2x)
    # Same type: 1x, Reverse: 0.5x
```

### c) Battle simulator
```python
def simulate_battle(pokemon1_stats, pokemon2_stats):
    """Simulate a full battle and return winner"""
    # Stats: {name, hp, attack, defense, speed, type}
```

Test with Charmander (Fire) vs Squirtle (Water)!

## Exercise 2: List Processing Functions
Implement these list manipulation functions WITHOUT using built-in functions like `sum()`, `max()`, `min()`, `sorted()`:

```python
def list_sum(numbers):
    """Return sum of all elements"""
    
def list_product(numbers):
    """Return product of all elements"""
    
def list_average(numbers):
    """Return average of all elements"""
    
def list_median(numbers):
    """Return median (middle value when sorted)"""
    
def list_mode(numbers):
    """Return most frequent value"""
    
def remove_duplicates(lst):
    """Return new list with duplicates removed, preserving order"""
```

## Exercise 3: Instagram Filter Engine 📸
Implement image operations using matrices (images are just 2D arrays!):

```python
def create_canvas(width, height, background_color=0):
    """Create a blank image canvas"""
    
def apply_brightness(image, factor):
    """Adjust brightness (multiply all pixels by factor)"""
    
def blur_filter(image):
    """Apply blur by averaging neighboring pixels"""
    
def edge_detection(image):
    """Detect edges using pixel differences"""
    
def rotate_90(image):
    """Rotate image 90 degrees clockwise"""
    
def create_gradient(width, height, direction='horizontal'):
    """Create a gradient effect"""
```

Test by creating ASCII art representations:
```python
# 0-3: ' ', 4-6: '.', 7-9: '*', 10+: '#'
image = [[0, 5, 10], [2, 7, 12], [4, 9, 14]]
# Displays as: " .#" / " *#" / ".*#"
```

## Exercise 4: Dictionary Operations
Create a student grade management system:

```python
def add_student(gradebook, name, grades):
    """Add a student with their grades to gradebook"""
    
def calculate_gpa(gradebook, name):
    """Calculate GPA for a specific student"""
    
def class_average(gradebook, subject):
    """Calculate class average for a specific subject"""
    
def top_students(gradebook, n=3):
    """Return top n students by GPA"""
    
def failing_students(gradebook, threshold=60):
    """Return list of students below threshold"""
```

Example gradebook structure:
```python
gradebook = {
    "Alice": {"Math": 95, "Physics": 88, "Chemistry": 92},
    "Bob": {"Math": 78, "Physics": 81, "Chemistry": 75}
}
```

## Exercise 5: Netflix Algorithm Simulator 🎬
Implement recommendation system algorithms:

### a) Watch history pattern finder
```python
def find_binge_pattern(watch_history, memo={}):
    """Find recurring viewing patterns using memoization"""
    # Return most common sequence of genres
```

### b) Recommendation tree builder
```python
def build_recommendation_tree(user_profile, content_library, depth=3):
    """Recursively build personalized recommendation paths"""
    # Each node leads to more specific suggestions
```

### c) Quick content search
```python
def search_content(library, title, filters=None):
    """Binary search through sorted content library"""
    # Filters: genre, year, rating
```

Test with:
- User who watched: ["Stranger Things", "Dark", "Black Mirror"]
- Should recommend: Sci-fi thrillers with mystery elements

## Exercise 6: Spotify Wrapped Generator 🎧
Analyze a year of listening data:

```python
def listening_stats(play_counts):
    """
    Analyze daily play counts and return your music personality:
    - 'total_minutes': Total listening time
    - 'peak_day': Your most active day
    - 'consistency': How regular your habits are
    - 'genre_evolution': How your taste changed
    - 'discovery_rate': New vs repeat songs
    - 'night_owl_score': Late night listening percentage
    """
    
def find_obsession_periods(songs, threshold=10, min_days=7):
    """
    Find when you played a song obsessively
    Return: {song: [(start_day, end_day, total_plays)]}
    """
    
def generate_music_seasons(listening_data):
    """
    Create your personal "music seasons":
    - 'Heartbreak Hotel': Sad songs period
    - 'Gym Rat Era': Workout music dominance
    - 'Study Grind': Lo-fi and classical
    - 'Party Animal': High energy phase
    """
```

## Exercise 7: Twitter Drama Analyzer 🔥
Analyze viral tweets and threads:

```python
def find_ratio_tweets(replies):
    """Find tweets that got 'ratio'd' (more replies than likes)"""
    
def extract_subtweeting(tweets):
    """Detect potential subtweeting patterns"""
    # Look for vague references, timing patterns
    
def viral_potential_score(tweet):
    """
    Calculate viral potential based on:
    - Emotional words
    - ALL CAPS percentage
    - Emoji density
    - Hot take indicators
    - Question marks (engagement bait)
    """
    
def thread_summarizer(thread):
    """Convert a 37-part thread into actual points"""
    # Return: main_point, supporting_args, unnecessary_parts
    
def detect_twitter_personalities(tweet_history):
    """
    Classify user type:
    - 'Reply Guy': High reply/original ratio
    - 'Hot Take Artist': Controversial opinions
    - 'Thread Philosopher': Long educational threads
    - 'Meme Lord': Image/joke heavy
    - 'Lurker': Rare poster
    """
```

## Exercise 8: TikTok Algorithm Battle ⚔️
Implement and race different feed-sorting algorithms:

```python
def engagement_sort(videos):
    """Sort by likes + comments + shares"""
    
def watch_time_sort(videos):
    """Sort by average completion rate"""
    
def personalized_sort(videos, user_preferences):
    """ML-style sort based on user history"""
    
def algorithm_showdown(content_pool, test_users):
    """
    Race algorithms to see which gets more 'engagement':
    - Generate feed for each algorithm
    - Simulate user scrolling
    - Measure 'addiction score' (time spent)
    - Crown the winner (most addictive algorithm)
    Return: {algorithm_name: {avg_watch_time, skip_rate, viral_discoveries}}
    """
```

Test with realistic data:
- Dance videos: High immediate engagement
- Educational: Slow burn, high completion
- Comedy: High shares, mixed completion

## Exercise 9: One-Line Coding Flexes 💪
Solve these using list comprehensions (impress your friends!):

```python
# 1. Generate Fibonacci sequence (first 20)
fib = # Your list comprehension dark magic here

# 2. Find all "nice" numbers (sum of digits equals 7) under 1000
nice_nums = # Your list comprehension here

# 3. Create a chess board (8x8) with 'B' and 'W' squares
chess = # Your nested comprehension here

# 4. Generate all possible pizza combinations
toppings = ['pepperoni', 'mushroom', 'olives']
combos = # Get all possible combinations (hint: use binary!)

# 5. Simulate dice probability (sum of two dice)
dice_sums = # Generate all possible sums and their frequency

# 6. Create ASCII art triangle
size = 5
triangle = # Generate: ['*', '**', '***', '****', '*****']

# 7. Find "happy numbers" (iterating sum of squares of digits reaches 1)
happy = # Find all happy numbers under 100
```

## Submission Instructions
- Submit your solutions in separate Python files for each exercise
- Include docstrings for all functions
- Add test cases demonstrating correctness
- Due: Before Week 5 lecture

## Grading Rubric
- Exercises 1-4: 12 points each
- Exercises 5-7: 11 points each
- Exercise 8: 10 points
- Exercise 9: 9 points
- **Total: 100 points**