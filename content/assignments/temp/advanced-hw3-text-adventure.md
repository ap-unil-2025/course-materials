---
layout: assignment
title: "Advanced HW3: Text Adventure Game Engine"
assignment_number: "HW3"
due_date: 2025-10-13 23:59:00
points: 150
difficulty: "Advanced"
estimated_time: "8-10 hours"
github_classroom_url: "https://classroom.github.com/a/advanced-hw3"
starter_repo: "ap2025-advanced-hw3-starter"
topics:
  - "Complex control flow"
  - "State management"
  - "String parsing"
  - "Game logic"
  - "File I/O"
bonus: true
status: "open"
---

## Overview

**This is an OPTIONAL grade booster assignment** worth 150 bonus points. Build a text-based adventure game engine using only Python basics (no functions or classes yet!). This challenges you to manage complex state and control flow.

## The Challenge: "Escape the Haunted Mansion"

Create a text adventure game where players navigate through a haunted mansion, solve puzzles, collect items, and escape. The game must be built using only the Python concepts from Week 3: variables, if/else, loops, and string manipulation.

## Learning Objectives

- Master complex nested control structures
- Manage game state with variables
- Parse and validate user input
- Implement game logic and puzzles
- Create engaging narrative experiences

## Part 1: Game World Setup (25 points)

### Room System
Without using lists or dictionaries, create a room system using variables:

```python
# Room 1: Entrance Hall
room1_name = "Entrance Hall"
room1_description = "A grand but dusty entrance hall. Cobwebs hang from the chandelier."
room1_exits_north = True  # Leads to room 2
room1_exits_south = False
room1_exits_east = True   # Leads to room 3
room1_exits_west = False
room1_item = "rusty_key"
room1_puzzle_solved = False

# Similar for rooms 2-10 (minimum)
```

### Requirements
- **Minimum 10 rooms** with unique descriptions
- Each room has up to 4 exits (north, south, east, west)
- Rooms must form a connected, explorable map
- Include at least 3 rooms that require items/puzzles to enter

## Part 2: Player State Management (25 points)

Track player state without lists:

```python
# Player state
player_current_room = 1
player_health = 100
player_moves = 0

# Inventory (up to 5 items)
inventory_slot1 = ""
inventory_slot2 = ""
inventory_slot3 = ""
inventory_slot4 = ""
inventory_slot5 = ""
inventory_count = 0

# Puzzle flags
has_solved_entrance_puzzle = False
has_solved_library_riddle = False
has_solved_basement_combination = False
# ... more puzzle flags

# Game flags
has_seen_ghost = False
has_found_secret_passage = False
has_triggered_trap = False
```

### Required Features
- Health system (player can take damage)
- Move counter (track number of actions)
- Inventory management (add/remove/use items)
- Multiple puzzle states
- Win/lose conditions

## Part 3: Command Parser (30 points)

Implement a robust command parser using only string methods and if/else:

```python
# Commands to support:
# - Movement: "go north", "north", "n", "move north"
# - Inventory: "inventory", "inv", "i"
# - Look: "look", "examine room", "l"
# - Take: "take key", "get key", "pick up key"
# - Use: "use key", "use key on door"
# - Help: "help", "h", "?"
# - Map: "map", "m" (show ASCII map)
# - Save/Load: "save game", "load game"
```

### Parsing Requirements
- Handle command variations (abbreviations, synonyms)
- Provide helpful error messages for invalid commands
- Case-insensitive input
- Handle multi-word items/commands
- Implement "undo" for last move

## Part 4: Puzzles and Challenges (35 points)

Implement at least 5 different puzzle types:

### 1. Riddle Puzzle (7 points)
```python
# Player must answer a riddle correctly
riddle = "I have cities, but no houses. I have mountains, but no trees. What am I?"
answer = "map"
```

### 2. Combination Lock (7 points)
```python
# Player must find clues to determine combination
# Clues scattered in different rooms
combination_digit1 = 4  # Found in library book
combination_digit2 = 2  # Written on bathroom mirror
combination_digit3 = 7  # Under kitchen table
```

### 3. Item Combination (7 points)
```python
# Combine two items to create new item
# Example: match + candle = lit_candle
```

### 4. Sequence Puzzle (7 points)
```python
# Player must perform actions in specific order
# Example: Pull lever A, then B, then A again
```

### 5. Timed Challenge (7 points)
```python
# Player has limited moves to escape a room
# Example: Room filling with water, 10 moves to escape
```

## Part 5: Game Features (25 points)

### ASCII Art and Presentation (5 points)
```python
# Title screen
print("""
╔══════════════════════════════════════╗
║   ESCAPE THE HAUNTED MANSION         ║
║   A Text Adventure Game              ║
╚══════════════════════════════════════╝
""")

# Room art (different for each room)
# ASCII map showing explored rooms
```

### Save/Load System (10 points)
Using file I/O, implement save/load:
- Save all game variables to a text file
- Load game state from file
- Multiple save slots (save1.txt, save2.txt, save3.txt)
- Autosave after important events

### Dynamic Narrative (10 points)
- Room descriptions change based on game state
- NPCs (ghosts/portraits) with different dialogues
- Multiple endings based on player actions
- Easter eggs and secret rooms

## Part 6: Bonus Features (10 points)

### Combat System (5 points)
Simple turn-based combat:
```python
ghost_health = 50
ghost_attack = 10
# Combat loop with attack/defend/flee options
```

### Achievement System (5 points)
Track player achievements:
```python
achievement_speed_runner = False  # Complete in under 50 moves
achievement_perfectionist = False  # Find all items
achievement_ghost_hunter = False  # Defeat all ghosts
achievement_puzzle_master = False  # Solve without hints
```

## Technical Requirements

### Code Organization
Despite not using functions, organize your code clearly:

```python
# ========================================
# GAME CONFIGURATION
# ========================================
GAME_TITLE = "Escape the Haunted Mansion"
VERSION = "1.0"
DEBUG_MODE = False

# ========================================
# ROOM DEFINITIONS
# ========================================
# Room 1: Entrance Hall
room1_name = "Entrance Hall"
# ... all room variables

# ========================================
# PLAYER STATE
# ========================================
# ... all player variables

# ========================================
# GAME ITEMS
# ========================================
# ... all item definitions

# ========================================
# MAIN GAME LOOP
# ========================================
game_running = True
while game_running:
    # Command input
    # Command parsing
    # Action execution
    # State updates
    # Win/lose checks
```

### Error Handling
Handle all edge cases:
- Invalid room transitions
- Inventory full
- Using items that don't exist
- Loading corrupted save files
- Invalid puzzle answers

## Deliverables

Submit a single Python file `haunted_mansion.py` containing:

1. **Complete game implementation** (one file, no functions/classes)
2. **Inline documentation** explaining game logic
3. **README.txt** with:
   - How to play
   - Command list
   - Walkthrough/solution
   - Map of the mansion
   - List of all puzzles and solutions

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Game World | 25 | 10+ rooms, connected map, descriptions |
| State Management | 25 | Player stats, inventory, puzzle flags |
| Command Parser | 30 | Robust input handling, error messages |
| Puzzles | 35 | 5 unique puzzle types, proper logic |
| Game Features | 25 | Save/load, ASCII art, narrative |
| Bonus Features | 10 | Combat and achievements |
| **Total** | **150** |

## Constraints and Rules

You may ONLY use:
- Variables (int, float, string, boolean)
- if/elif/else statements
- while and for loops
- String methods (split, strip, lower, etc.)
- print() and input()
- File I/O (open, read, write)
- Basic operators (+, -, *, /, //, %, ==, !=, etc.)

You may NOT use:
- Functions (def)
- Classes
- Lists, tuples, sets, dictionaries
- Import statements (except for random if needed)
- Global keyword
- Lambda, map, filter
- Any advanced Python features

## Tips for Success

- **Plan your game map on paper first**
- **Use meaningful variable names** (room3_has_key not r3hk)
- **Test edge cases** (what if player types gibberish?)
- **Create a debug mode** to help testing
- **Save your work frequently** (version control!)

## Example Gameplay

```
══════════════════════════════════════════
ESCAPE THE HAUNTED MANSION
══════════════════════════════════════════

You wake up in a dusty entrance hall. The door behind you is locked.
Cobwebs hang from an ornate chandelier. There's something glinting on the floor.

> look
You're in the Entrance Hall. Exits: North, East
You see: a rusty key

> take key
You pick up the rusty key.

> inventory
You are carrying: rusty key (1/5 items)

> go north
The door is locked. Perhaps you need a key?

> use rusty key
You unlock the door with the rusty key.

> go north
You enter the Library...
```

## Academic Integrity

This is an individual assignment. You may discuss game design ideas but must implement all code yourself. Using functions/classes or copying code will result in a zero.

## Submission

1. Test your game thoroughly
2. Include walkthrough in README.txt
3. Submit `haunted_mansion.py` and `README.txt` via GitHub Classroom
4. Ensure game runs on Python 3.10+

---

*This is an optional grade booster. Successfully completing this challenging assignment demonstrates mastery of basic Python concepts and creative problem-solving.*