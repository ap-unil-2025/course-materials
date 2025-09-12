---
title: "Problem Set - Week 3"
date: 2025-10-06
description: "Python Basics - Variables, Control Flow, and Simple Programs"
---

# Problem Set 3: Python Fundamentals

This problem set will help you practice the Python basics covered in Week 3.

## Exercise 1: Mars Weather Station 🚀
You're programming a weather station for the Mars colony! Write a program that:
1. Asks for the current Mars temperature (in Celsius)
2. Converts to Earth equivalents (Fahrenheit and Kelvin)
3. Determines if it's a "nice day" on Mars (above -60°C is considered nice!)
4. Checks if CO₂ would be solid (dry ice forms below -78.5°C)
5. Warns if spacesuits are mandatory (below -50°C)
6. Celebrates if it's warm enough for liquid water (above 0°C - extremely rare!)

**Fun fact**: Mars temperatures range from -143°C to 35°C. Test your program with -80°C (typical Mars winter)

## Exercise 2: Crypto Investment Simulator 💰
You've discovered a time machine and want to simulate Bitcoin investments! Write a program that:

1. Asks how much money you would have invested (in USD)
2. Asks what year you would have bought (2010-2023)
3. Uses these historical Bitcoin prices:
   - 2010: $0.10
   - 2011: $1
   - 2013: $100
   - 2015: $250
   - 2017: $1,000
   - 2019: $4,000
   - 2021: $30,000
   - 2023: $25,000
4. Calculate how many Bitcoin you could have bought
5. Show the value at each subsequent year
6. Display your best and worst decisions
7. Add dramatic messages like "You're a millionaire!" or "HODL! 💎🙌"

**Reality check**: $100 invested in 2010 = 1000 BTC = $25 million in 2023!

## Exercise 3: Secret Agent Code Generator 🕵️
You're a secret agent who needs prime numbers for encryption! Write a program that:
1. Asks for your agent number (any positive integer)
2. Checks if your agent number is "prime" (secure) or "composite" (compromised)
3. If compromised, finds who can decode it (smallest divisor = enemy agent number)
4. Generates your "safe communication channels" (all primes less than your number)
5. Creates a "security score" (percentage of numbers below yours that are prime)
6. Assigns code names based on primality:
   - Prime: "Shadow Wolf"
   - Even composite: "Double Agent"
   - Odd composite: "Rogue Operator"

**Mission briefing**: Agent 007 is prime and secure. Agent 008 is compromised by Agent 002!

## Exercise 4: Debugging Practice
The following programs contain errors. Identify and fix them:

### a) Area of a circle
```python
import math
radius = input("Enter radius: ")
area = math.pi * radius ^ 2
print(f"Area = area")
```

### b) Quadratic formula
```python
# Solve ax^2 + bx + c = 0
a = 1, b = -5, c = 6
discriminant = b**2 - 4ac
x1 = -b + discriminant**0.5 / 2*a
x2 = -b - discriminant**0.5 / 2*a
print("Solutions:", x1, x2)
```

### c) Fibonacci sequence
```python
# Print first 10 Fibonacci numbers
a = 0
b = 1
count = 0
while count < 10
    print(a)
    a = b
    b = a + b
    count += 1
```

## Exercise 5: Hogwarts Grade Calculator ⚡
You're calculating grades at Hogwarts School! Create a program that:
1. Asks for scores in three subjects:
   - Defense Against Dark Arts (0-100)
   - Potions (0-100)
   - Transfiguration (0-100)
2. Asks for Quidditch performance (0-100, counts as homework)
3. Asks for House participation points (0-100)
4. Calculate weighted average (same weights as before)
5. Assign magical grades:
   - Outstanding (O): 90-100 "You're the chosen one!"
   - Exceeds Expectations (E): 80-89 "Hermione would be proud!"
   - Acceptable (A): 70-79 "You pass, muggle!"
   - Poor (P): 60-69 "Needs more Felix Felicis"
   - Dreadful (D): 50-59 "Troll in the dungeon!"
   - Troll (T): Below 50 "Worse than Crabbe and Goyle"
6. Award or deduct house points based on performance
7. Determine if student makes the Quidditch team (needs O or E)

## Exercise 6: Dragon's Treasure Hunt 🐉
A dragon has hidden treasure! Create an adventure game:
1. The dragon thinks of a number between 1 and 100 (the treasure location)
2. You have 7 attempts before the dragon wakes up!
3. After each guess, the dragon growls hints:
   - Too high: "The treasure lies deeper in the cave..."
   - Too low: "Climb higher, adventurer..."
   - Very close (within 5): "The dragon's breathing gets heavier..."
   - Very far (>30 away): "You feel lost in the darkness..."
4. Track your path through the cave (all guesses)
5. Victory: Show your bravery rating (fewer attempts = braver)
   - 1-2 attempts: "Dragon Slayer!"
   - 3-4 attempts: "Treasure Hunter!"
   - 5-6 attempts: "Lucky Adventurer!"
   - 7 attempts: "Narrow Escape!"
6. Defeat: The dragon wakes! Show where the treasure was
7. Calculate your "explorer efficiency" (how close your average guess was)

## Exercise 7: Pyramid of Power 🔺
Build the ancient Pyramid of Power where each stone has magical properties!
1. Ask the architect how many levels to build (1-15)
2. Each stone's power equals the sum of the two stones above it
3. The pyramid reveals magical patterns:
   - Each row sum is a power of 2 (show this!)
   - The diagonal shows counting numbers
   - Row 5 contains the sacred sequence: 1, 4, 6, 4, 1
4. Color code the output (using text):
   - Powers of 2: Show with [brackets]
   - Perfect squares: Show with *asterisks*
   - Others: Normal display
5. Calculate the "total pyramid power" (sum of all numbers)
6. Reveal if it's a "Perfect Pyramid" (rows = 7 or 11, considered lucky)

**Ancient wisdom**: Row 7 contains 1, 6, 15, 20, 15, 6, 1 - all divisible by row number 7!

## Exercise 8: Alien Message Decoder 👽
You've intercepted an alien transmission! Analyze it:
1. Ask for the intercepted message
2. Decode its properties:
   - Word count ("transmission units")
   - Vowel frequency ("harmonic resonance")
   - Consonant count ("dissonance factor")
   - Numbers found ("coordinate markers")
   - Space gaps ("quantum separators")
3. Identify the "power word" (longest) and "key word" (shortest)
4. Reverse engineer the message (print it backwards)
5. Create a transmission pyramid for analysis
6. Determine the message type:
   - >50% vowels: "Peaceful greeting"
   - >5 numbers: "Star coordinates"
   - All caps: "DISTRESS SIGNAL!"
   - Contains 'help': "Rescue request"
   - Otherwise: "Unknown intent"
7. Calculate "translation confidence" (% of recognizable patterns)

**Test transmission**: "HELP 42 we come in peace from ZORG-7"

## Submission Instructions
- Submit a single Python file `problem_set_3.py` with all solutions
- Each exercise should be clearly marked with comments
- Include test cases showing your programs work correctly
- Due: Before Week 4 lecture

## Grading Rubric
- Exercise 1-3: 15 points each
- Exercise 4: 10 points
- Exercise 5-6: 15 points each
- Exercise 7-8: 10 points each
- Code style and comments: 5 points
- **Total: 100 points**